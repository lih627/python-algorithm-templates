"""
携程海洋馆中有 n 只萌萌的小海豚，初始均为 0 岁，
每只小海豚的寿命是 m 岁，且这些小海豚会在 birthYear[i]
这些年份生产出一位宝宝海豚（1 <= birthYear[i] <= m），
每位宝宝海豚刚出生为 0 岁。
问 x 年时，携程海洋馆有多少只小海豚？

输入
n（初始海豚数）
m（海豚寿命）
海豚生宝宝的年份数量 (假设为 p)
海豚生宝宝的年份 1
...
海豚生宝宝的年份 p
x（几年后）

输出
x 年后，共有多少只小海豚

样例:
5
5
2
2
4
5

输出
20
"""


def solve(n, m, indexs, x):
    """
    ij 表示 第i年j岁的小海豚
    DP[i][j] = DP[i-1][j-1]
    DP[i][0] = sum(DP[i][age], age in ages)
    压缩到 只需要 pre 和 cur
    """
    pre = [0] * (m + 1)
    pre[0] = n
    for i in range(x):
        cur = [0] * (m + 1)
        for j in range(1, m + 1):
            cur[j] = pre[j - 1]
        for idx in indexs:
            cur[0] += cur[idx]
        pre = cur[:]
    return sum(cur)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    p = int(input())
    years = []
    for i in range(p):
        years.append(int(input()))
    x = int(input())
    print(solve(n, m, years, x))
