class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        maximum_moves = c - b - 1 + b - a - 1
        if c - b == 1 and b - a == 1:
            minimum_moves = 0
        elif c - b == 2 or b - a == 2:
            minimum_moves = 1
        elif c - b == 1 or b - a == 1:
            minimum_moves = 1
        else:
            minimum_moves = 2

        return [minimum_moves, maximum_moves]
