class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        delete = []
        a_len = len(A)
        s_len = len(A[0])
        if a_len <= 1:
            return 0
        mark = [0] * s_len
        i = 1
        while i < a_len:
            pre = A[i - 1]
            cur = A[i]
            for j in range(s_len):
                if pre[j] == cur[j] or mark[j] == 1:
                    continue
                if pre[j] > cur[j]:
                    mark[j] = 1
                    i = 0
                    break
                break
            i += 1
        return sum(mark)
