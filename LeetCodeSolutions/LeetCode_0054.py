class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == [[]]:
            return []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        res = []
        size = m * n
        cnt = 0
        while True:
            res.extend(matrix[cnt][cnt: n - cnt][:])
            print(res)
            if len(res) == size:
                return res
            for _ in range(cnt + 1, m - cnt):
                res.append(matrix[_][n - cnt - 1])
            print(res)
            if len(res) == size:
                return res
            tmp = [matrix[m - cnt - 1][_] for _ in range(n - cnt - 2, cnt - 1, -1)]
            res.extend(tmp[:])
            if len(res) == size:
                return res

            for _ in range(m - cnt - 2, cnt, -1):
                res.append(matrix[_][cnt])
            if len(res) == size:
                return res
            cnt += 1
