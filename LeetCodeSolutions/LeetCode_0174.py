class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0
        row, col = len(dungeon), len(dungeon[0])
        dp = [0] * col
        dp[-1] = dungeon[-1][-1]
        for j in range(col - 2, - 1, - 1):
            if dp[j + 1] > 0:
                dp[j] = dungeon[-1][j]
                continue
            dp[j] = dungeon[-1][j] + dp[j + 1]
        for i in range(row - 2, -1, -1):
            for j in range(col - 1, -1, -1):
                if j == col - 1:
                    if dp[j] <= 0:
                        dp[j] += dungeon[i][j]
                    else:
                        dp[j] = dungeon[i][j]
                else:
                    if dp[j] > 0 or dp[j + 1] > 0:
                        dp[j] = dungeon[i][j]
                    else:
                        dp[j] = dungeon[i][j] + max(dp[j], dp[j + 1])
        return 1 if dp[0] > 0 else abs(dp[0]) + 1
