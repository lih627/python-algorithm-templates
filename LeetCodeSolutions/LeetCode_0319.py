class Solution:
    def bulbSwitch(self, n: int) -> int:
        """
        返回 完全平方数的个数
        """
        if not n:
            return 0
        return int(n ** 0.5)
