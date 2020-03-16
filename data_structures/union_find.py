class DSU:
    """
    Disjoint Union Set
    并查集
    LeetCode 547
    """

    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        '''
        不使用路径压缩
        '''
        while self.parent[x] != -1:
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        self.parent[rootx] = rooty

    def findCircleNum(self):
        return self.parent.count(-1)


class UF:
    """
    from LeetCode lucifer
    """

    parent = {}
    cnt = 0

    def __init__(self, M):
        n = len(M)
        for i in range(n):
            self.parent[i] = i
            self.cnt += 1

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q): return
        self.parent[self.find(p)] = self.find(q)
        self.cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)
