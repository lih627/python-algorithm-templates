class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        row, col = len(matrix), len(matrix[0])
        dp = [0] * col
        ret = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0
            left = []
            right = [None] * col
            stack = []
            for idx, val in enumerate(dp):
                while stack and val <= dp[stack[-1]]:
                    stack.pop();
                if not stack:
                    left.append(-1)
                else:
                    left.append(stack[-1])
                stack.append(idx)
            stack = []
            for idx, val in enumerate(dp[::-1]):
                cidx = col - idx - 1
                while stack and val <= dp[stack[-1]]:
                    stack.pop();
                if not stack:
                    right[cidx] = col
                else:
                    right[cidx] = stack[-1]
                stack.append(cidx)
            for l, r, v in zip(left, right, dp):
                ret = max(ret, v * (r - l - 1))
        return ret
