import time, copy, random

MAXLIFE = 100000
MAXMACHINES = 30

class Plane(object):
    """
    p should be a list of strings, such that
    p[0][0] -> plane[(0,0)]

    zero = (i,j) shifts the origin so that 
    p[i][j] -> plane[(0,0)]
    """
    def __init__(self, p=[], zero=(0,0)):
        self.plane = {}
        for y, l in enumerate(p):
            for x, v in enumerate(l):
                if v == ' ':
                    continue
                self.plane[(x-zero[0], y-zero[1])] = v

    def __getitem__(self, key):
        try:
            return self.plane[key]
        except KeyError:
            return None

    def __setitem__(self, key, value):
        self.plane[key] = value
        if value is None:
            del self.plane[key]

    def __iter__(self):
        return self.plane.__iter__()

    def __next__(self):
        return self.plane.__next__()

    def getbounds(self):
        k = self.plane.keys()

        if len(k) == 0:
            return [0,0,0,0]

        c = list(zip(*k))
        return [min(c[0]), max(c[0]), min(c[1]), max(c[1])]

    def __str__(self):
        self.bounds = self.getbounds()

        out = ""
        for y in range(self.bounds[2], self.bounds[3] + 1):
            for x in range(self.bounds[0], self.bounds[1] + 1):
                if self[(x,y)] is not None:
                    out += self[(x,y)]
                else:
                    out += ' '
            out += '\n'

        return out


class Rule(object):
    def __init__(self, newstate='q0', newsym=['E'], direction='L', spawn=False, sp_off=(0,0), sp_state=None):
        self.newsym = newsym
        self.newstate = newstate
        self.direction = direction
        self.spawn = spawn
        self.sp_off = sp_off
        self.sp_state = sp_state

    def __repr__(self):
        return "(" + str(self.newstate) + ", " + str(self.newsym) + ", " + self.direction + ")" 


class MachineContext(object):
    def __init__(self, tape):
        self.tape = tape
        self.running = []
        self.halted = []
        self.delay = 0

    def checkpoint(self):
        self.copy = copy.deepcopy(self)

    def restore(self):
        self = self.copy
        self.checkpoint()
        return self

    def get_machine_col(cls, machine):
        mhash = hash(machine.path)

        return (mhash%0x100,
                (mhash//0x100)%0x100,
                (mhash//0x10000)%0x100)

    def create_machine(self, path, pos=None, state=None, lifespan=MAXLIFE, parent=None):
        if len(self.running) > MAXMACHINES: 
            return

        youngling = None

        for machine in self.halted:
            if path == machine.path:
                youngling = machine
                break

        if youngling:
            youngling.reset()
            youngling.lifespan = lifespan
            if pos:
                youngling.pos = pos
            if state:
                youngling.state = state

            self.running.insert(self.running.index(parent) if parent else 0, youngling)
            self.halted.remove(youngling)
            return

        for machine in self.running:
            if path == machine.path:
                youngling = Machine(machine.path,
                                    machine.rules,
                                    machine.start,
                                    lifespan,
                                    self.tape)
                if pos:
                    youngling.pos = pos
                if state:
                    youngling.state = state
                youngling.context = self

        if not youngling:
            youngling = parse_machine(path, lifespan)
            youngling.tape = self.tape
            if pos:
                youngling.pos = pos
            if state:
                youngling.state = state
            youngling.context = self
                
        self.running.insert(self.running.index(parent) if parent else 0, youngling)
        youngling.color = self.get_machine_col(youngling)

    def add_machine(self, machine):
        if len(self.running) > MAXMACHINES: 
            return

        machine.color = self.get_machine_col(machine)
        self.running.insert(0,machine)
        machine.context = self

    def step(self):
        for i in range(len(self.running) - 1, -1, -1):
            machine = self.running[i]
            machine.advance()
            if machine.halted:
                self.halted.append(machine)
                del self.running[i]
    
    def run(self, display=True):
        while self.running: 
            self.step()
            if display:
                print(self.running)
                print(self.tape, end='\n\n')
                time.sleep(self.delay)

class Machine(object):
    def __init__(self, path, rules, start='q0', lifespan=MAXLIFE, tape=None):
        self.path = path
        self.rules = rules
        self.start = start
        self.state = start
        self.lifespan = lifespan
        self.context = None

        if not tape:
            self.tape = Plane()
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
        self.tape[self.pos] = random.choice(op.newsym)
        self.state = op.newstate

        if op.spawn:
            offpath = "/".join(self.path.split('/')[:-1] + [op.spawn])

            offspring = parse_machine(offpath, self.lifespan - self.i)
            offspring.tape = self.tape
            offspring.pos = self.get_offset_pos(op)
            
            if not self.context:
                self.context = MachineContext(self.tape)
                self.context.delay = self.delay
                self.context.add_machine(self)
                self.context.create_machine(offpath, self.get_offset_pos(op), op.sp_state if op.sp_state else None, self.lifespan - self.i, self)
                self.move_sequence(op.direction)
                self.context.run()
            else:
                self.context.create_machine(offpath, self.get_offset_pos(op), op.sp_state if op.sp_state else None, self.lifespan - self.i, self)
                
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
        print(self.tape, end='\n\n')

    def __repr__(self):
        return "<" + self.path.split('/')[-1] + ": " + self.state + ", " + str(self.pos) + ">" 

def parse_machine(path, maxiter=MAXLIFE):
    btck_to_none = lambda c: None if c == '`' else c

    with open(path, 'r', encoding='utf-8') as f:
        startstate = f.readline()
        while startstate[0] == '#' or startstate == '\n':
            startstate = f.readline()
        startstate = startstate.strip()
        
        rules = {}
        rule = f.readline()

        # Rule format: state s -> newstate n M [childpath [xoff,yoff]]
        while rule != '':
            if rule != '\n' and rule.strip()[0] != '#':
                rule = rule.strip().split()
                for s in rule[1]:
                    rules[(rule[0], btck_to_none(s))] = Rule(rule[3], 
                                                             [btck_to_none(s) if c == '~' else btck_to_none(c) for c in rule[4]], 
                                                             rule[5], 
                                                             False if len(rule) < 7 else rule[6],
                                                             (0,0) if len(rule) < 8 else [int(x) for x in rule[7].split(',')],
                                                             None if len(rule) < 9 else rule[8])

            rule = f.readline()

        return Machine(path, rules, startstate, lifespan=maxiter)
