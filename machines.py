import time
import tapes

MAXITER = 1000

class Rule(object):
    def __init__(self, newstate='q0', newsym='e', direction='L', spawn=False, sp_off=(0,0)):
        self.newsym = newsym
        self.newstate = newstate
        self.direction = direction
        self.spawn = spawn
        self.sp_off = sp_off

    def __repr__(self):
        return "(" + str(self.newstate) + ", " + str(self.newsym) + ", " + self.direction + ")" 


class LMachine(object):
    def __init__(self, rules, start='q0'):
        self.rules = rules
        self.start = start
        self.state = start
        self.tape = tapes.Tape()
        self.pos = 0
        self.i = 0
        self.children = []
        self.halted = False

    def left(self):
        self.pos -= 1
    
    def right(self):
        self.pos += 1

    def advance(self):
        if self.halted:
            return

        op = self.rules[(self.state, self.tape[self.pos])]
        self.tape[self.pos] = op.newsym
        self.state = op.newstate
        if op.direction == 'L':
            self.left()
        elif op.direction == 'R':
            self.right()

        if op.spawn:
            self.children.append(parse_machine(op.spawn))

        if 'H' in op.direction:
            self.halted = True
            raise StopIteration("Halting machine.")

    def cont(self, display=False, delay=0):
        while self.i < MAXITER and not self.halted:
            self.i += 1
            try:
                if display:
                    self.print_state()
                self.advance()
                time.sleep(delay)
            except StopIteration:
                break
            except KeyError:
                break

    def run(self, tape, pos=0, display=True, delay=0):
        self.state = self.start
        self.tape = tape
        self.pos = pos
        self.i = 0
        self.halted = False
        self.cont(display, delay)

    def print_state(self):
        print(end=' ')
        for v in self.tape:
            if v is not None:
                print(v, end='')
            else:
                print(' ', end='')
        print(' ' + self.state)
        print((self.pos + abs(self.tape.negmin) + 1)*' ' + '^')


class PMachine(object):
    def __init__(self, rules, start='q0'):
        self.rules = rules
        self.start = start
        self.state = start
        self.plane = tapes.Plane()
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
    
    def advance(self):
        if self.halted:
            return

        op = self.rules[(self.state, self.plane[self.pos])]
        self.plane[self.pos] = op.newsym
        self.state = op.newstate
        
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

        for c in self.children:
            c.advance()
            if c.halted:
                self.children.extend(c.children)
        self.children = [c for c in self.children if not c.halted]

        if op.spawn:
            offspring = parse_machine(op.spawn)
            offspring.plane = self.plane
            offspring.pos = (self.pos[0]+op.sp_off[0], self.pos[1]+op.sp_off[1])
            self.children.append(offspring)

    def cont(self, display=False, delay=0):
        while self.i < MAXITER and not self.halted:
            self.i += 1
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

    def run(self, plane, pos=(0,0), display=False, delay=0):
        self.state = self.start
        self.plane = plane
        self.pos = pos
        self.i = 0
        self.halted = False
        self.cont(display, delay)

    def print_state(self):
        print(self.state, self.pos)
        print(self.plane, end='\n\n')

def parse_machine(filename):
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
                    rules[(rule[0], btck_to_none(s))] = Rule(rule[3], btck_to_none(s) if rule[4] == '~' else btck_to_none(rule[4]), rule[5], False if len(rule) < 7 else rule[6])
                    if len(rule) > 7:
                        rules[(rule[0], btck_to_none(s))].sp_off = tuple([int(x) for x in rule[7].split(',')])

            rule = f.readline()

        if t == 'L':
            return LMachine(rules, startstate)
        elif t == 'P':
            return PMachine(rules, startstate)
