class Solution:
    def convertToTitle(self, n: int) -> str:
        nums = list(range(1, 27))
        alphas = [chr(_) for _ in range(ord('A'), ord('Z') + 1)]
        d = dict(zip(nums, alphas))
        d[0] = 'Z'
        res = ''
        while n > 0:
            div = n // 26
            mod = n - div * 26
            if mod == 0:
                div = (n - 26) // 26
            res = d[mod] + res
            n = div
        return res
