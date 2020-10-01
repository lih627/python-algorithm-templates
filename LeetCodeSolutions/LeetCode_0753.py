class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        highest = 10 ** (n - 1)
        ret = []

        def dfs(node):
            for x in range(k):
                _node = node * 10 + x
                if _node not in seen:
                    seen.add(_node)
                    dfs(_node % highest)
                    ret.append(str(x))

        dfs(0)
        # print(ret)
        return ''.join(ret) + '0' * (n - 1)
