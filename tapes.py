"""
    This represents a tape, infinite in both directions.
    Blank squares are represented by the None type.
    Supports normal list indexing.
"""
class Tape(object):
    """
    Input to the tape constructor is a string: one symbol per character.
    Spaces represent blank squares.
    """
    def __init__(self, t='', shift=0):
        self.pos = [None if v == ' ' else v for v in t[shift:]]
        self.neg = [None if v == ' ' else v for v in t[:shift]]
        self.negmin = self.last_filled_index(False)
        self.posmax = self.last_filled_index()

    def __iter__(self):
        self.index = self.negmin
        return self

    def __next__(self):
        if self.index > self.posmax:
            raise StopIteration

        value = self[self.index]
        self.index += 1
        return value
    
    def expand_lists(self, i):
        if i >= 0:
            while i >= len(self.pos):
                self.pos += [None]*(len(self.pos)+1)
        else:
            while abs(i) > len(self.neg):
                self.neg = [None]*(len(self.neg)+1) + self.neg

    def shrink_lists(self):
        return
        if abs(self.negmin) < len(self.neg)/3 and len(self.neg) > 10:
            self.neg = self.neg[len(self.neg)/2:]
        if self.posmax < len(self.pos)/3 and len(self.pos) > 10:
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
                if v is not None:
                    break
                l += 1
            return l - len(self.neg)

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
            self.negmin = self.last_filled_index(False)
            self.posmax = self.last_filled_index()
            #self.shrink_lists()

    def __str__(self):
        return str(['' if x is None else x for x in self.neg[self.negmin:]]) + str(['' if x is None else x for x in self.pos[:self.posmax + 1]])


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
