class DSU:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def un(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parents[ry] = rx

    def counter(self):
        return len(set([self.find(x) for x in self.parents]))


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        dsu = DSU(n)
        for a, b in edges:
            dsu.un(a, b)
        return dsu.counter() == 1
