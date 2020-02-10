class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [[] for _ in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            if i == 0:
                ans[i] = [1]
            else:
                ans[i] = [1] * (i + 1)

        if rowIndex > 1:
            for i in range(2, rowIndex + 1):
                j = 1
                while (j < i):
                    ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
                    j += 1
        return ans[rowIndex]
