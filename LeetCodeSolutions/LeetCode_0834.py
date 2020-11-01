from collections import defaultdict


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        sz = [0] * N
        dp = [0] * N
        ret = [0] * N

        def dfs1(node, parent):
            for son in graph[node]:
                if son == parent:
                    continue
                dfs1(son, node)
                sz[node] += sz[son]
                dp[node] += dp[son]
            dp[node] += sz[node]
            sz[node] += 1

        def dfs2(node, parent):
            ret[node] = dp[node]
            for son in graph[node]:
                if son == parent:
                    continue
                ssz, psz = sz[son], sz[node]
                sdp, pdp = dp[son], dp[node]
                dp[node] = dp[node] - dp[son] - sz[son]
                sz[node] -= sz[son]
                dp[son] = dp[son] + dp[node] + sz[node]
                sz[son] += sz[node]
                dfs2(son, node)
                sz[son], sz[node] = ssz, psz
                dp[son], dp[node] = sdp, pdp

        dfs1(0, -1)
        dfs2(0, -1)
        return ret
