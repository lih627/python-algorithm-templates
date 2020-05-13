class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        a = [[val, idx] for idx, val in enumerate(A)]
        b = [[val, idx] for idx, val in enumerate(B)]
        a.sort(key=lambda x: x[0])
        b.sort(key=lambda x: x[0])
        pairs = []
        idxA = 0
        n = len(A)
        not_used = n - 1
        for elem_b in b:
            b_val, b_idx = elem_b
            while idxA < n and a[idxA][0] <= b_val:
                pairs.append([a[idxA][1], b[not_used][1]])
                not_used -= 1
                idxA += 1
            if idxA == n:
                break
            else:
                pairs.append([a[idxA][1], b_idx])
                idxA += 1
        res = [None] * n
        for a, b in pairs:
            res[b] = A[a]
        return res
