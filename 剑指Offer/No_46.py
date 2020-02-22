class Solution:
    def translateNum(self, num: int) -> int:
        cnt = 0

        def helper(s):
            nonlocal cnt
            if not s:
                cnt += 1
                return
            helper(s[1:])
            if len(s) > 1:
                if '09' < s[:2] < '26':
                    helper(s[2:])

        helper(str(num))
        return cnt
