'''
LeetCode No.64
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes
 the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

Time: O(mn)
Space: O(n)
'''

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            # grid = []
            return None
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for idx, val in enumerate(grid[0]):
            if idx == 0:
                dp[idx] = val
                continue
            dp[idx] = dp[idx - 1] + val

        # i = 1 ... m -1, j = 0 ... n - 1
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(solution.minPathSum(grid))
