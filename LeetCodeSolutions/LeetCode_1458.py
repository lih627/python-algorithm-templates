class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[float('-inf') for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    if j == 0:
                        dp[i][j] = nums2[i] * nums1[j]
                    else:
                        dp[i][j] = max(nums2[i] * nums1[j], dp[i][j - 1])
                    continue
                if j == 0:
                    dp[i][j] = max(nums1[j] * nums2[i], dp[i - 1][j])
                    continue
                dp[i][j] = max((dp[i - 1][j - 1] + (nums1[j] * nums2[i])), nums1[j] * nums2[i], dp[i][j - 1],
                               dp[i - 1][j])
        return dp[-1][-1]
