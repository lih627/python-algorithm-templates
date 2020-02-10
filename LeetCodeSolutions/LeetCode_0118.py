class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = [[] for _ in range(numRows)]
        for i in range(numRows):
            if i == 0:
                ans[i] = [1]
            else:
                ans[i] = [1] * (i + 1)

        if numRows > 2:
            for i in range(2, numRows):
                j = 1
                while (j < i):
                    ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
                    j += 1
        return ans
