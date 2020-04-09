class Solution:
    def nextGreaterElement(self, n: int) -> int:
        str_n = list(str(n))
        n = len(str_n)
        if n < 2:
            return -1
        i = n - 1
        idx = -1
        while i - 1 > -1:
            if str_n[i] > str_n[i - 1]:
                idx = i - 1
                break
            i -= 1
        if idx == -1:
            return -1
        j = n - 1
        while j > idx:
            if str_n[j] > str_n[idx]:
                break
            j -= 1
        str_n[idx], str_n[j] = str_n[j], str_n[idx]
        l = idx + 1
        r = n - 1
        while l < r:
            str_n[l], str_n[r] = str_n[r], str_n[l]
            l += 1
            r -= 1
        res = int(''.join(str_n))
        return res if res >> 31 == 0 else -1
