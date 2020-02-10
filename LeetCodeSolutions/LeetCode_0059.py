class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        tmp = list(range(1, n ** 2 + 1))
        cnt = 0
        while True:
            for _ in range(cnt, n - cnt):
                res[cnt][_] = tmp.pop(0)
            if not tmp:
                return res

            for _ in range(cnt + 1, n - cnt):
                res[_][n - cnt - 1] = tmp.pop(0)
            if not tmp:
                return res

            for _ in range(n - cnt - 2, cnt - 1, -1):
                res[n - cnt - 1][_] = tmp.pop(0)
            if not tmp:
                return res

            for _ in range(n - cnt - 2, cnt, -1):
                res[_][cnt] = tmp.pop(0)
            if not tmp:
                return res
            cnt += 1
