# encoding: utf-8
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

class MachineContext(object):
    def __init__(self, tape):
        self.tape = tape
        self.running = []
        self.halted = []
        self.delay = 0

    def create_machine(self, path, pos=None, lifespan=MAXLIFE, parent=None):
        youngling = None

        for machine in self.halted:
            if path == machine.name:
                youngling = machine
                break

        if youngling:
            youngling.reset()
            youngling.lifespan = lifespan
            if pos:
                youngling.pos = pos

            self.running.insert(self.running.index(parent) if parent else 0, youngling)
            self.halted.remove(youngling)
            return

        for machine in self.running:
            if path == machine.name:
                youngling = Machine(machine.name,
                                    machine.rules,
                                    machine.start,
                                    machine.linear,
                                    lifespan,
                                    self.tape)
                youngling.pos = pos
                youngling.context = self

        if not youngling:
            youngling = parse_machine(path, lifespan)
            youngling.tape = self.tape
            if pos:
                youngling.pos = pos
            youngling.context = self
                
        self.running.insert(self.running.index(parent) if parent else 0, youngling)

    def add_machine(self, machine):
        self.running.insert(0,machine)
        machine.context = self

    def run(self, display=True):
        while self.running: 
            for i in range(len(self.running) - 1, -1, -1):
                machine = self.running[i]
                machine.advance()
                if machine.halted:
                    self.halted.append(machine)
                    del self.running[i]

            if display:
                print(self.running)
                print(self.tape, end='\n\n')
                time.sleep(self.delay)

class Machine(object):
    def __init__(self, name, rules, start='q0', linear=False, lifespan=MAXLIFE, tape=None):
        self.name = name
        self.rules = rules
        self.start = start
        self.state = start
        self.linear = linear
        self.lifespan = lifespan
        self.context = None

        if linear:
            if not tape:
                self.tape = tapes.Tape()
            else:
                self.tape = tape
            self.pos = 0
            self.left = self.linleft
            self.right = self.linright
            self.print_state = self.linprint
        else:
            if not tape:
                self.tape = tapes.Plane()
            else:
                self.tape = tape
            self.pos = (0,0)

        self.i = 0
        self.delay = 0
        self.halted = False

    def reset(self):
        self.state = self.start
        self.lifespan = MAXLIFE
        self.i = 0
        self.halted = False
        self.delay = 0
        if self.linear:
            self.pos = 0
        else:
            self.pos = (0,0)

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

    def move_sequence(self, moves):
        for m in moves:
            if m == 'L':
                self.left()
            elif m == 'R':
                self.right()        
            elif m == 'U':
                self.up()
            elif m == 'D':
                self.down()
            elif m == 'H':
                self.halted = True
                return

    def advance(self):
        if self.halted:
            return

        self.i += 1

        op = self.rules[(self.state, self.tape[self.pos])]
        self.tape[self.pos] = op.newsym
        self.state = op.newstate

        if op.spawn:
            offspring = parse_machine(op.spawn, self.lifespan - self.i)
            offspring.tape = self.tape
            offspring.pos = self.get_offset_pos(op)
            
            if not self.context:
                self.context = MachineContext(self.tape)
                self.context.delay = self.delay
                self.context.add_machine(self)
                self.context.create_machine(op.spawn, self.get_offset_pos(op), self.lifespan - self.i)
                self.move_sequence(op.direction)
                self.context.run()
            else:
                self.context.create_machine(op.spawn, self.get_offset_pos(op), self.lifespan - self.i, self)
                

        self.move_sequence(op.direction)

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
        self.delay = delay
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

    def __repr__(self):
        return "<" + self.name.split('/')[-1] + ": " + self.state + ", " + str(self.pos) + ">" 

def parse_machine(filename, maxiter=MAXLIFE):
    btck_to_none = lambda c: None if c == '`' else c

    with open(filename, 'r', encoding='utf-8') as f:
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
            return Machine(filename, rules, startstate, linear=True, lifespan=maxiter)
        elif t == 'P':
            return Machine(filename, rules, startstate, lifespan=maxiter)
