from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for idx, val in enumerate(A):
            if idx == 0:
                continue
            if val <= A[idx - 1]:
                res += A[idx - 1] + 1 - val
                A[idx] = A[idx - 1] + 1
        return res

    def minIncrementForUnique2(self, A: List[int]) -> int:
        """
        计数
        """
        cnt = [0] * 40001
        max_value = 0
        for num in A:
            cnt[num] += 1
            if num > max_value:
                max_value = num
        move = 0
        for j in range(max_value):
            if cnt[j] > 1:
                move += cnt[j] - 1
                cnt[j + 1] += cnt[j] - 1

        if cnt[max_value] > 1:
            d = cnt[max_value] - 1
            move += (1 + d) * d // 2
        return move

    def minIncrementForUnique3(self, A: List[int]) -> int:
        """
        路径压缩
        """
        pos = [None] * 80000
        cnt = 0

        def helper(idx):
            if pos[idx] is None:
                pos[idx] = idx
                return idx
            idx2 = helper(pos[idx] + 1)
            pos[idx] = idx2
            return idx2

        for num in A:
            cnt += helper(num) - num
        return cnt
