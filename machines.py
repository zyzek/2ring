import time
import tapes

MAXITER = 10000

class Rule(object):
    def __init__(self, newstate='q0', newsym='e', direction='L'):
        self.newsym = newsym
        self.newstate = newstate
        self.direction = direction

    def __repr__(self):
        return "(" + str(self.newstate) + ", " + str(self.newsym) + ", " + self.direction + ")" 


class LMachine(object):
    def __init__(self, rules, start='q0'):
        self.rules = rules
        self.start = start
        self.state = start
        self.tape = tapes.Tape()
        self.position = 0

    def left(self):
        self.position -= 1
    
    def right(self):
        self.position += 1

    def advance(self):
        op = self.rules[(self.state, self.tape[self.position])]
        self.tape[self.position] = op.newsym
        self.state = op.newstate
        if op.direction == 'L':
            self.left()
        else:
            self.right()

    def run(self, tape, position=0, delay=0, print=True):
        self.state = self.start
        self.tape = tape
        self.position = position
        i = 0
        while i < MAXITER:
            i += 1
            try:
                if print:
                    self.print_state()
                self.advance()
                time.sleep(delay)
            except Exception as e:
                #print(e)
                break 

    def print_state(self):
        print(end=' ')
        for v in self.tape:
            if v is not None:
                print(v, end='')
            else:
                print(' ', end='')
        print(' ' + self.state)
        print((self.position + abs(self.tape.negmin) + 1)*' ' + '^')


class PMachine(object):
    def __init__(self, rules, start='q0'):
        self.rules = rules
        self.start = start
        self.state = start
        self.plane = tapes.Plane()
        self.pos = (0,0)

    def left(self):
        self.pos = (self.pos[0] - 1, self.pos[1])
    
    def right(self):
        self.pos = (self.pos[0] + 1, self.pos[1])

    def up(self):
        self.pos = (self.pos[0], self.pos[1] - 1)

    def down(self):
        self.pos = (self.pos[0], self.pos[1] + 1)
    
    def advance(self):
        op = self.rules[(self.state, self.plane[self.pos])]
        self.tape[self.pos] = op.newsym
        self.state = op.newstate
        if op.direction == 'L':
            self.left()
        elif op.direction == 'R':
            self.right()
        elif op.direction == 'U':
            self.up()
        else:
            self.down()

    def run(self, plane, position=(0,0), delay=0):
        self.state = self.start
        self.plane = plane
        self.position = position
        i = 0
        while i < MAXITER:
            i += 1
            try:
                self.print_state()
                self.advance()
                time.sleep(delay)
            except Exception as e:
                #print(e)
                break 

    def print_state(self):
        print(end=' ')
        for v in self.tape:
            if v is not None:
                print(v, end='')
            else:
                print(' ', end='')
        print(' ' + self.state)
        print((self.position + abs(self.tape.negmin) + 1)*' ' + '^')


def parse_machine(filename):
    with open(filename, 'r') as f:
        t = f.readline()
        while t[0] == '#':
            t = f.readline().strip()

        startstate = f.readline().strip()
        rules = {}
        rule = f.readline()

        while rule != '':
            rule = rule.strip().split()
            rules[(rule[0], None if rule[1] == '`' else rule[1])] = Rule(rule[3], None if rule[4] == '`' else rule[4], rule[5])
            rule = f.readline()

        if t == 'L':
            return LMachine(rules, startstate)
        elif t == 'P':
            return PMachine(rules, startstate)
