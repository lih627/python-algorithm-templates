"""
A 和 B 两人在抽奖, 现在有一个抽奖箱, 里面有n张中奖票
m 张不中奖票, A 和 B 轮流从中抽出一张奖票, 如果有人抽中奖票
他讲获得胜利. 其余奖票将被丢弃.
额外的, B 每次抽奖后, 会再次抽取一张牌扔掉.
现在 A 先抽, 请问 A 的胜率, 保持小数点4位有有效数字

输入 n m
输出 A 的胜率

360 2020笔试
"""


def solve(n, m):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(0, m + 1):
            if i == 0:
                continue
            elif j == 0:
                dp[i][j] = 1
            elif j == 1:
                # 对于j = 1 张不中奖票 和 i 张中奖票
                # A 必须第一次就中奖
                # A 中奖概率 为 i/(j + 1)
                dp[i][j] = i / (i + j)
            elif j == 2:
                # 对于 j = 2 张不中奖票 和 i 张中奖票
                # A 可以第一轮中奖 + A第一轮不中奖的概率 * 在(i - 1, j - 2) 情况下的中奖概率
                dp[i][j] = i / (i + j) + \
                           j / (i + j) * (j - 1) / (i + j - 1) * dp[i - 1][j - 2]
            else:
                dp[i][j] = i / (i + j) + \
                           j / (i + j) * (j - 1) / (i + j - 1) * \
                           (
                                   i / (i + j - 2) * dp[i - 1][j - 2] + \
                                   (j - 2) / (i + j - 2) * dp[i][j - 3]
                           )

    return round(dp[-1][-1], 4)


if __name__ == '__main__':
    n, m = map(int, input().split())
    print('{:.4f}'.format(solve(n, m)))
