"""
LeetCode 1135:
Find MST in Graph
"""


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.parent[rx] = ry

    def isCircle(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        dsu = DSU(N)
        cnt = 0
        ret = 0
        for edges in connections:
            if not dsu.isCircle(edges[0], edges[1]):
                cnt += 1
                ret += edges[2]
                dsu.union(edges[0], edges[1])
            if cnt == N - 1:
                break
        return ret if cnt == N - 1 else -1
