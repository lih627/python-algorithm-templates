class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        res = []
        low = [-1] * n
        graph = [[] for _ in range(n)]
        for (i, j) in connections:
            graph[i].append(j)
            graph[j].append(i)

        cur = 1

        def targan(node, parent=None):
            nonlocal cur
            dfn = low[node] = cur
            cur += 1
            for son in graph[node]:
                if son != parent:
                    if low[son] == -1:
                        targan(son, node)
                        if dfn < low[son]:
                            res.append([son, node])
                    low[node] = min(low[son], low[node])

        targan(0)
        return res
