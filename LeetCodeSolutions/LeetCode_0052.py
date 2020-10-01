class Solution:
    def totalNQueens(self, n: int) -> int:
        ret = 0

        def helper(idx):
            nonlocal ret, valid
            if idx == n:
                ret += 1
                return
            for k in range(n):
                if (idx, k) in valid:
                    tmp = set()
                    for r in range(n):
                        if (r, k) in valid:
                            tmp.add((r, k))
                    for c in range(n):
                        if (idx, c) in valid:
                            tmp.add((idx, c))
                    x, y = idx, k
                    while -1 < x < n and -1 < y < n:
                        if (x, y) in valid:
                            tmp.add((x, y))
                        x -= 1
                        y -= 1
                    x, y = idx, k
                    while -1 < x < n and -1 < y < n:
                        if (x, y) in valid:
                            tmp.add((x, y))
                        x += 1
                        y += 1
                    x, y = idx, k
                    while -1 < x < n and -1 < y < n:
                        if (x, y) in valid:
                            tmp.add((x, y))
                        x -= 1
                        y += 1
                    x, y = idx, k
                    while -1 < x < n and -1 < y < n:
                        if (x, y) in valid:
                            tmp.add((x, y))
                        x += 1
                        y -= 1
                    valid -= tmp
                    helper(idx + 1)
                    valid = valid.union(tmp)

        valid = set()
        for i in range(n):
            for j in range(n):
                valid.add((i, j))
        helper(0)
        return ret
