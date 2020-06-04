class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        cnt = 0
        for idx, val in enumerate(s):
            if idx == 0:
                cnt += 1
                continue
            if val == s[idx - 1]:
                cnt += 1
                res = max(res, cnt)
            else:
                res = max(res, cnt)
                cnt = 1
        return res
