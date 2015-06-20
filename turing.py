import time

LEFT = 0
RIGHT = 1

DELAY = 0.01
class TapeIterator(object):
    def __init__(self, tape):
        self.tape = tape
        self.index = self.tape.negmin

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.tape.posmax:
            raise StopIteration

        value = self.tape[self.index]
        self.index += 1
        return value

class Tape(list):
    def __init__(self, pos=[], neg=[]):
        self.pos = pos
        self.neg = neg
        self.negmin = self.last_filled_index(False)
        self.posmax = self.last_filled_index()

    def expand_lists(self, i):
        if i >= 0:
            while i >= len(self.pos):
                self.pos += [None]*(len(self.pos)+1)
        else:
            while abs(i) > len(self.neg):
                self.neg = [None]*(len(self.neg)+1) + self.neg

    def shrink_lists(self):
        if self.negmin > len(self.neg)/3:
            self.neg = self.neg[len(self.neg)/2:]
        if self.posmax < len(self.neg)/3:
            self.pos = self.pos[:len(self.pos)/2]

    def last_filled_index(self, p=True):
        if p:
            l = len(self.pos)
            for v in self.pos[::-1]:
                l -= 1
                if v is not None:
                    break
            return l
        else:
            l = 0
            for v in self.neg:
                l -= 1
                if v is not None:
                    break
            return l
    
    def __delitem__(self, key):
        if key >= 0:
            del self.pos[key]
            if key == self.posmax and self.posmax >= 0:
                self.posmax = last_filled_index()
        else:
            del self.neg[key]
            if key == self.negmin and self.negmin <= -1:
                self.negmin = last_filled_index(False)

        self.shrink_lists()

    def __getitem__(self, key):
        self.expand_lists(key)

        if key >= 0:
            return self.pos[key]
        else:
            return self.neg[key]

    def __setitem__(self, key, value):
        self.expand_lists(key)

        if key >= 0:
            self.pos[key] = value
            if value is not None and key > self.posmax:
                self.posmax = key
        else:
            self.neg[key] = value
            if value is not None and key < self.negmin:
                self.negmin = key

        if value is None and (key == self.negmin or key == self.posmax):
            self.shrink_lists()

    def __str__(self):
        return str(['' if x is None else x for x in self.neg[self.negmin:]]) + str(['' if x is None else x for x in self.pos[:self.posmax + 1]])


class Rule(object):
    def __init__(self, newstate='q0', newsym='e', direction=LEFT):
        self.newsym = newsym
        self.newstate = newstate
        self.direction = direction


class LMachine(object):
    maxiter = 10000
    def __init__(self, rules, tape=Tape(), start='q0', position=0):
        self.tape = tape
        self.state = start
        self.rules = rules
        self.position = position

    def left(self):
        self.position -= 1
    
    def right(self):
        self.position += 1

    def advance(self):
        op = self.rules[(self.state, self.tape[self.position])]
        self.tape[self.position] = op.newsym
        self.state = op.newstate
        if op.direction == LEFT:
            self.left()
        else:
            self.right()

    def run(self):
        i = 0
        while i < self.maxiter:
            i += 1
            try:
                self.print_state()
                self.advance()
                time.sleep(DELAY)
            except Exception as e:
                #print(e)
                break 

    def print_state(self):
        print(end=' ')
        for v in TapeIterator(self.tape):
            if v is not None:
                print(v, end='')
            else:
                print(' ', end='')
        print(' ' + self.state)
        print((self.position + abs(self.tape.negmin) + 1)*' ' + '^')


u_rules = {}
u_rules[('q0', 0)] = Rule('q0', 0, RIGHT)
u_rules[('q0', 1)] = Rule('q1', 0, RIGHT)
u_rules[('q1', 0)] = Rule('q1', 0, RIGHT)
u_rules[('q1', None)] = Rule('q2', None, LEFT)
u_rules[('q2', 0)] = Rule('done', None, LEFT)

u_tape = Tape([0,0,0,0,1,0,0,0])
u_add = LMachine(u_rules, u_tape)
#u_add.run()

b_rules = {}
b_rules[('LSB1', 0)] = Rule('LSB1', 0, RIGHT)
b_rules[('LSB1', 1)] = Rule('LSB1', 1, RIGHT)
b_rules[('LSB1', 2)] = Rule('LSB1', 2, RIGHT)
b_rules[('LSB1', '|')] = Rule('LSB1', '|', RIGHT)
b_rules[('LSB1', ',')] = Rule('D1', ',', LEFT)

b_rules[('D1', 0)] = Rule('LSB2-0', ',', RIGHT)
b_rules[('D1', 1)] = Rule('LSB2-1', ',', RIGHT)
b_rules[('D1', '|')] = Rule('LSB2-F', '|', RIGHT)

b_rules[('LSB2-0', 0)] = Rule('LSB2-0', 0, RIGHT)
b_rules[('LSB2-0', 1)] = Rule('LSB2-0', 1, RIGHT)
b_rules[('LSB2-0', ',')] = Rule('LSB2-0', ',', RIGHT)
b_rules[('LSB2-0', ';')] = Rule('D2-0', ';', LEFT)
b_rules[('LSB2-1', 0)] = Rule('LSB2-1', 0, RIGHT)
b_rules[('LSB2-1', 1)] = Rule('LSB2-1', 1, RIGHT)
b_rules[('LSB2-1', ',')] = Rule('LSB2-1', ',', RIGHT)
b_rules[('LSB2-1', ';')] = Rule('D2-1', ';', LEFT)
b_rules[('LSB2-F', 0)] = Rule('LSB2-0', 0, RIGHT)
b_rules[('LSB2-F', 1)] = Rule('LSB2-0', 1, RIGHT)
b_rules[('LSB2-F', ',')] = Rule('LSB2-F', ',', RIGHT)
b_rules[('LSB2-F', ';')] = Rule('D2-F', ';', LEFT)

b_rules[('D2-0', 0)] = Rule('S-0', ';', LEFT)
b_rules[('D2-0', 1)] = Rule('S-1', ';', LEFT)
b_rules[('D2-0', ',')] = Rule('S-0', ',', LEFT)
b_rules[('D2-1', 0)] = Rule('S-1', ';', LEFT)
b_rules[('D2-1', 1)] = Rule('S-2', ';', LEFT)
b_rules[('D2-1', ',')] = Rule('S-1', ',', LEFT)
b_rules[('D2-F', 0)] = Rule('S-0', ';', LEFT)
b_rules[('D2-F', 1)] = Rule('S-1', ';', LEFT)
b_rules[('D2-F', ',')] = Rule('LSBC', ',', LEFT)

b_rules[('S-0', 0)] = Rule('S-0', 0, LEFT)
b_rules[('S-0', 1)] = Rule('S-0', 1, LEFT)
b_rules[('S-0', 2)] = Rule('S-0', 2, LEFT)
b_rules[('S-0', ',')] = Rule('S-0', ',', LEFT)
b_rules[('S-0', '|')] = Rule('S-0', '|', LEFT)
b_rules[('S-0', None)] = Rule('LSB1', 0, RIGHT)
b_rules[('S-1', 0)] = Rule('S-1', 0, LEFT)
b_rules[('S-1', 1)] = Rule('S-1', 1, LEFT)
b_rules[('S-1', 2)] = Rule('S-1', 2, LEFT)
b_rules[('S-1', ',')] = Rule('S-1', ',', LEFT)
b_rules[('S-1', '|')] = Rule('S-1', '|', LEFT)
b_rules[('S-1', None)] = Rule('LSB1', 1, RIGHT)
b_rules[('S-2', 0)] = Rule('S-2', 0, LEFT)
b_rules[('S-2', 1)] = Rule('S-2', 1, LEFT)
b_rules[('S-2', 2)] = Rule('S-2', 2, LEFT)
b_rules[('S-2', ',')] = Rule('S-2', ',', LEFT)
b_rules[('S-2', '|')] = Rule('S-2', '|', LEFT)
b_rules[('S-2', None)] = Rule('LSB1', 2, RIGHT)

b_rules[('LSBC', 0)] = Rule('LSBC', 0, LEFT)
b_rules[('LSBC', 1)] = Rule('LSBC', 1, LEFT)
b_rules[('LSBC', ',')] = Rule('LSBC', ',', LEFT)
b_rules[('LSBC', '|')] = Rule('CLSB', '|', LEFT)

b_rules[('CLSB', 0)] = Rule('C-0', 0, LEFT)
b_rules[('CLSB', 1)] = Rule('C-0', 1, LEFT)
b_rules[('CLSB', 2)] = Rule('C-1', 0, LEFT)
b_rules[('CLSB', None)] = Rule('done', 0, LEFT)

b_rules[('C-0', 0)] = Rule('C-0', 0, LEFT)
b_rules[('C-0', 1)] = Rule('C-0', 1, LEFT)
b_rules[('C-0', 2)] = Rule('C-1', 0, LEFT)
b_rules[('C-0', None)] = Rule('done', None, RIGHT)

b_rules[('C-1', 0)] = Rule('C-0', 1, LEFT)
b_rules[('C-1', 1)] = Rule('C-1', 0, LEFT)
b_rules[('C-1', 2)] = Rule('C-1', 1, LEFT)
b_rules[('C-1', None)] = Rule('done', 1, LEFT)

b_tape = Tape(pos=[1,1,0,1,',',1,1,0,0,1,';'],neg=['|'])
b_tape2 = Tape(pos=[',',';'],neg=['|'])
b_tape3 = Tape(pos=[1,',',';'],neg=['|'])
b_tape4 = Tape(pos=[',',1,';'],neg=['|'])
b_tape5 = Tape(pos=[0,',',';'],neg=['|'])
b_tape6 = Tape(pos=[',',0,';'],neg=['|'])
b_tape = Tape(pos=[1,0,0,0,0,1,1,1,0,0,1,1,0,',',1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,';'],neg=['|'])

b_add = LMachine(b_rules, tape=b_tape, start='LSB1')
b_add.run()
#47823
#4326

#52149