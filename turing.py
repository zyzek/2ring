import time

LEFT = 0
RIGHT = 1
DELAY = 0.01

# TODO: Integrate into the Tape class
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
"""
	This represents a tape, infinite in both directions.
	Blank squares are represented by the None type.
	Supports normal list indexing.
"""
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

    def __repr__(self):
    	return "(" + str(self.newstate) + ", " + str(self.newsym) + ", " + ("L" if self.direction == LEFT else "R") + ")" 


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
                print(e)
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


def parse_machine(filename):

	with open(filename, 'r') as f:
		t = f.readline()
		while t[0] == '#':
			t = f.readline().strip()

		if t == 'L':
			startstate = f.readline().strip()
			position = int(f.readline().strip())
			pretape = f.readline().strip()
			neg = [None if x == '`' else x for x in pretape[:position]]
			pos = [None if x == '`' else x for x in pretape[position:]]
			tape = Tape(pos, neg)
			rules = {}
			rule = f.readline()

			while rule != '':
				rule = rule.strip().split()
				rules[(rule[0], None if rule[1] == '`' else rule[1])] = Rule(rule[3], None if rule[4] == '`' else rule[4], RIGHT if rule[5] == 'R' else LEFT)
				rule = f.readline()

			print(tape)
			print(rules)
			print(startstate)

			return LMachine(rules, tape, startstate)



m = parse_machine("machines/unaryadder.tm")
m.run()

b_add = parse_machine("machines/binaryadder.tm")
b_add.run()

"""
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

"""