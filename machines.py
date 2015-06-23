import time
import tapes

MAXLIFE = 1000

class Rule(object):
    def __init__(self, newstate='q0', newsym='e', direction='L', spawn=False, sp_off=(0,0)):
        self.newsym = newsym
        self.newstate = newstate
        self.direction = direction
        self.spawn = spawn
        self.sp_off = sp_off

    def __repr__(self):
        return "(" + str(self.newstate) + ", " + str(self.newsym) + ", " + self.direction + ")" 

class Machine(object):
    def __init__(self, rules, start='q0', linear=False, lifespan=MAXLIFE):
        self.rules = rules
        self.start = start
        self.state = start
        self.linear = linear
        self.lifespan = lifespan

        if linear:
            self.tape = tapes.Tape()
            self.pos = 0
            self.left = self.linleft
            self.right = self.linright
            self.print_state = self.linprint
        else:
            self.tape = tapes.Plane()
            self.pos = (0,0)

        self.i = 0
        self.delay = 0
        self.children = []
        self.halted = False

    def left(self):
        self.pos = (self.pos[0] - 1, self.pos[1])
    
    def right(self):
        self.pos = (self.pos[0] + 1, self.pos[1])

    def up(self):
        self.pos = (self.pos[0], self.pos[1] - 1)

    def down(self):
        self.pos = (self.pos[0], self.pos[1] + 1)

    def linleft(self):
        self.pos -= 1

    def linright(self):
        self.pos += 1
    
    def get_offset_pos(self, op):
        if self.linear:
            return self.pos+op.sp_off[0]
        else:
            return (self.pos[0]+op.sp_off[0], self.pos[1]+op.sp_off[1])

    def advance(self):
        if self.halted:
            return

        self.i += 1

        op = self.rules[(self.state, self.tape[self.pos])]
        self.tape[self.pos] = op.newsym
        self.state = op.newstate

        for c in self.children:
            c.advance()
            if c.halted:
                self.children.extend(c.children)
        self.children = [c for c in self.children if not c.halted]

        if op.spawn:
            offspring = parse_machine(op.spawn, self.lifespan - self.i)
            offspring.tape = self.tape
            offspring.pos = self.get_offset_pos(op)
            self.children.append(offspring)
        
        for d in op.direction:
            if d == 'L':
                self.left()
            elif d == 'R':
                self.right()        
            elif d == 'U':
                self.up()
            elif d == 'D':
                self.down()
            elif d == 'H':
                self.halted = True
                break

        if self.i >= self.lifespan:
            self.halted = True

    def cont(self, display=False, delay=0):
        while not self.halted: 
            try:
                if display:
                    self.print_state()
                self.advance()
                time.sleep(delay)
            except KeyError as e:
                print(e)
                break
        if display:
            self.print_state()

    def run(self, tape, pos, display=False, delay=0):
        self.state = self.start
        self.tape = tape
        self.pos = pos
        self.i = 0
        self.halted = False
        self.cont(display, delay)

    def print_state(self):
        #print(self.state, self.pos)
        print(self.tape, end='\n\n')

    def linprint(self):
        print(end=' ')
        for v in self.tape:
            if v is not None:
                print(v, end='')
            else:
                print(' ', end='')
        print(' ' + self.state)
        print((self.pos + abs(self.tape.negmin) + 1)*' ' + '^')

def parse_machine(filename, maxiter=MAXLIFE):
    btck_to_none = lambda c: None if c == '`' else c

    with open(filename, 'r') as f:
        t = f.readline()
        while t[0] == '#' or t == '\n':
            t = f.readline()
        t = t.strip()

        startstate = f.readline()
        while startstate[0] == '#' or startstate == '\n':
            startstate = f.readline()
        startstate = startstate.strip()
        
        rules = {}
        rule = f.readline()

        while rule != '':
            if rule != '\n' and rule[0] != '#':
                rule = rule.strip().split()
                for s in rule[1]:
                    rules[(rule[0], btck_to_none(s))] = Rule(rule[3], 
                                                             btck_to_none(s) if rule[4] == '~' else btck_to_none(rule[4]), 
                                                             rule[5], 
                                                             False if len(rule) < 7 else rule[6])
                    if len(rule) > 7:
                        rules[(rule[0], btck_to_none(s))].sp_off = [int(x) for x in rule[7].split(',')]

            rule = f.readline()

        if t == 'L':
            return Machine(rules, startstate, linear=True, lifespan=maxiter)
        elif t == 'P':
            return Machine(rules, startstate, lifespan=maxiter)
