class Solution:
    def maximum(self, a: int, b: int) -> int:
        return (abs(a - b) + a + b) // 2
