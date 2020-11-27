class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        used = set([''])
        c = list(tiles)
        v = [False] * len(c)
        ret = 0

        def helper(cur):
            nonlocal ret
            if cur not in used:
                ret += 1
                used.add(cur)
            for idx, v_ in enumerate(v):
                if not v_:
                    v[idx] = True
                    helper(cur + c[idx])
                    v[idx] = False

        helper('')
        return ret
