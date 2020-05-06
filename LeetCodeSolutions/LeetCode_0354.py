from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: [x[0], -x[1]])

        def lcs(nums):
            cells = []
            for idx, val in enumerate(nums):
                if not cells or val > cells[-1]:
                    cells.append(val)
                    continue
                cells[bisect_left(cells, val)] = val
            return len(cells)

        nums = [_[1] for _ in envelopes]
        return lcs(nums)
