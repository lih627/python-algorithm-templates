class Solution:
    def twoSum(self, n: int) -> List[float]:
        l = 6 * n + 1
        dp = [0] * l
        dp[1: 7] = [1] * 6
        left = 1
        for i in range(2, n + 1):
            left = i
            right = i * 6
            while right >= left:
                _ = right - 6 if right >= 6 else 0
                dp[right] = sum(dp[_: right])
                right -= 1
            print('1', dp)
            dp[:left] = [0] * left
        res = dp[left:]
        all_nums = 6 ** n
        res = [_ / all_nums for _ in res]
        return res
