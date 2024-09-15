from itertools import zip_longest

class AlternateArray:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def rearrange(self):
        pos = [x for x in self.arr if x > 0]
        neg = [x for x in self.arr if x < 0]
        if len(pos) > len(neg):
            pos, neg = neg, pos
        pos = pos + [0] * (len(neg) - len(pos))
        return [x for pair in zip_longest(neg, pos) for x in pair]