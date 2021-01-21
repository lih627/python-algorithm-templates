class Solution:
    def maskPII(self, S: str) -> str:
        s = S.lower()
        if '@' in s:
            t = s.split('@')
            t[0] = t[0][0] + '*' * 5 + t[0][-1]
            return '@'.join(t)
        else:
            t = []
            for c in s:
                if '0' <= c <= '9':
                    t.append(c)
            n = len(t)
            t = ''.join(t[-4:])
            if n == 10:
                return '***-***-' + t
            elif n == 11:
                return '+*-***-***-' + t
            elif n == 12:
                return '+**-***-***-' + t
            else:
                return '+***-***-***-' + t
