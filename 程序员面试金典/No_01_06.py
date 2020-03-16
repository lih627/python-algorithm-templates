class Solution:
    def compressString(self, S: str) -> str:
        i = j = 0
        n = len(S)
        res = ''
        cnt = 0
        while i < n:
            if j == n:
                res += str(j - i)
                break
            if i == j:
                res += S[i]
                j += 1
            elif S[i] == S[j]:
                j += 1
            else:
                res += str(j - i)
                i = j
        if len(res) < n:
            return res
        else:
            return S
