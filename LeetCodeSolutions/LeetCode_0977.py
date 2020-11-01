class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: abs(x))
        return [i ** 2 for i in A]
