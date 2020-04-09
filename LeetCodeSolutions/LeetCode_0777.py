class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        L = R = 0
        for i in range(n):
            s, e = start[i], end[i]
            if s == 'R':
                if L != 0:
                    return False
                else:
                    R += 1
            if e == 'R':
                if R == 0 or L != 0:
                    return False
                else:
                    R -= 1
            if e == 'L':
                if R != 0:
                    return False
                else:
                    L += 1

            if s == 'L':
                if L == 0 or R != 0:
                    return False
                else:
                    L -= 1
        return L == 0 and R == 0
