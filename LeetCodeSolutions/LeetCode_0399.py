class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = collections.defaultdict(dict)
        for idx, (a, b) in enumerate(equations):
            d[a][b] = values[idx]
            d[b][a] = 1 / values[idx]
        for k in d:
            d[k][k] = 1.0
        res = []

        def dfs(a, b):
            if a not in d or b not in d:
                return -1.0
            if a == b:
                return 1.0

        def bfs(a, b):
            if a not in d or b not in d:
                return -1.0
            if a == b:
                return 1.0
            que = collections.deque()
            visited = set([a])
            que.append([a, 1.0])
            while que:
                cur, tmp = que.popleft()
                for s in d[cur]:
                    if s == b:
                        return tmp * d[cur][s]
                    else:
                        if s not in visited:
                            visited.add(s)
                            que.append([s, tmp * d[cur][s]])
            return -1.0

        res = [bfs(a, b) for a, b in queries]
        return res
