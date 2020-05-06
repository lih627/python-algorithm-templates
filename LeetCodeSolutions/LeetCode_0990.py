class DSU:
    def __init__(self):
        self.parent = [_ for _ in range(26)]

    def find(self, s):
        s_id = ord(s) - ord('a')
        while self.parent[s_id] != s_id:
            self.parent[s_id] = self.parent[self.parent[s_id]]
            s_id = self.parent[s_id]
        return s_id

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        else:
            self.parent[root_a] = root_b


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equals = [[_[0], _[3]] for _ in equations if _[1] == '=']
        nequals = [[_[0], _[3]] for _ in equations if _[1] == '!']
        dsu = DSU()
        for a, b in equals:
            dsu.union(a, b)

        for a, b in nequals:
            if dsu.find(a) == dsu.find(b):
                return False
        return True
