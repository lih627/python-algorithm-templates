class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k or k == 0 or n < 1:
            return []
        if n == k:
            return [list(range(1, n + 1))]
        elems = list(range(1, n + 1))
        res = []

        def helper(idx, cur_num, tmp):
            if cur_num == k:
                for _ in range(idx, n):
                    res.append(tmp + [elems[_]])
                return
            for _ in range(idx, n):
                helper(_ + 1, cur_num + 1, tmp + [elems[_]])

        helper(0, 1, [])
        return res
