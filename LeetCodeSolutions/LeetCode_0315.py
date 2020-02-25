class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def __lowbit(self, index):
        return index & (- index)

    def update(self, index, delta):
        while index < self.size + 1:
            self.tree[index] += delta
            index += self.__lowbit(index)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.__lowbit(index)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 1:
            return []
        if n == 1:
            return [0]
        s = list(set(nums))
        total_rank = len(s)
        rank_map = {}
        import heapq
        heapq.heapify(s)
        for _ in range(1, total_rank + 1):
            rank_map[heapq.heappop(s)] = _
        res = []
        ft = FenwickTree(total_rank)
        for _ in range(n - 1, -1, -1):
            index = rank_map[nums[_]]
            ft.update(index, 1)
            res = [ft.query(index - 1)] + res
        return res
