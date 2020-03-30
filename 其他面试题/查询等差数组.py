"""
给定一个矩阵，每行是等差数列，
但是有部分值是被隐藏了的，数值为 0 即是被隐藏了，
根据输入的值 i，j，
判断这个位置上的值是否可以被推导出来，
可以就输出，否则输出 Unknown
"""


def trans(A, n, m):
    """
    遍历一次行,
    遍历一次列
    把能填的数字填上
    计算不出来的为None
    然后直接查询, None 输出 Unknown
    """
    row = n
    col = m
    for i in range(row):
        for j in range(col):
            if A[i][j] == 0:
                A[i][j] = None

    for i in range(row):
        has_num = set()
        for j in range(col):
            if A[i][j] is not None:
                has_num.add((i, j))
            if len(has_num) == 2:
                pos1, pos2 = list(has_num)
                val1 = A[pos1[0]][pos1[1]]
                val2 = A[pos2[0]][pos2[1]]
                delta = (val2 - val1) // (pos2[1] - pos1[1])
                for k in range(col):
                    if A[i][k] is None:
                        A[i][k] = val1 + delta * (k - pos1[1])
                break
    for j in range(col):
        has_num = set()
        for i in range(row):
            if A[i][j] is not None:
                has_num.add((i, j))
            if len(has_num) == 2:
                pos1, pos2 = list(has_num)
                val1 = A[pos1[0]][pos1[1]]
                val2 = A[pos2[0]][pos2[1]]
                delta = (val2 - val1) // (pos2[0] - pos1[0])
                for k in range(row):
                    if A[k][j] is None:
                        A[k][j] = val1 + delta * (k - pos1[0])


if __name__ == '__main__':
    n, m, q = map(int, input().split())
    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    trans(A, n, m)
    for j in range(q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if A[x][y] is not None:
            print(A[x][y])
        else:
            print('Unknown')
