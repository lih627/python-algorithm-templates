import collections


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = collections.Counter(moves)
        if counter.get('U', 0) != counter.get('D', 0):
            return False
        if counter.get('L', 0) != counter.get('R', 0):
            return False
        return True
