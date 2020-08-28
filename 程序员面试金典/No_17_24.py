class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        prefix = [matrix[i][:] for i in range(row)]
        for i in range(row):
            for idx, val in enumerate(prefix[i]):
                if idx == 0:
                    continue
                prefix[i][idx] += prefix[i][idx - 1]
        ans = [-1, -1, -1, -1]
        cprefix = [0] * row
        rmax = float('-inf')
        for y1 in range(col):
            for y2 in range(y1, col):
                if y1 == 0:
                    for k in range(row):
                        cprefix[k] = prefix[k][y2]
                else:
                    for k in range(row):
                        cprefix[k] = prefix[k][y2] - prefix[k][y1 - 1]
                # print("y1 {}, y2 {}, cprefix:{}".format(y1, y2, cprefix))
                x1, x2 = 0, 0
                premax = cprefix[0]
                if premax > rmax:
                    rmax = premax
                    ans = [x1, y1, x2, y2]
                    # print('rmax: {}, ans: {}'.format(rmax, ans))
                x2 += 1
                while x2 < row:
                    if premax < 0:
                        x1 = x2
                        cmax = cprefix[x2]
                    else:
                        cmax = cprefix[x2] + premax
                    premax = cmax
                    if cmax > rmax:
                        rmax = cmax
                        ans = [x1, y1, x2, y2]
                        # print('rmax: {}, ans: {}'.format(rmax, ans))
                    x2 += 1
        return ans
