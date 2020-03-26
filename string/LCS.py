"""
Longest Common Sbusequence
最长公共字符列长度
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3
"""


def lcs(text1, text2):
    '''
    DP
    '''
    len1 = len(text1)
    len2 = len(text2)
    dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
