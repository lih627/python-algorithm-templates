class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp algorithm
        l = len(s)
        if l < 2:
            return s

        dp = [[False for i in range(l)] for _ in range(l)]
        for i in range(l):
            dp[i][i] = True

        res_len = 0
        idx1 = 0
        idx2 = 0

        for j in range(l):
            for i in range(0, j + 1):
                if j - i < 3:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and j - i > res_len:
                    res_len = j - i
                    idx1 = i
                    idx2 = j
        return s[idx1: idx2 + 1]

    def longestPalindrome_(self, s: str) -> str:
        # Expand Around Center
        tmp = list(s)
        insrts = ' '.join(tmp)

        def findpalindromic(idx, s):
            center = s[idx]
            left = idx - 1
            right = idx + 1
            while (
                    left > -1
                    and right < len(s)
                    and s[left] == s[right]):
                center = s[left] + center + s[right]
                left -= 1
                right += 1
            center = center.split()
            res = ''.join(center)
            return res, len(res)

        i = 0
        res = ''
        minl = 0
        while i < len(insrts):
            tmp, curl = findpalindromic(i, s=insrts)
            if curl > minl:
                minl = curl
                res = tmp
            i += 1
        return res
