import random
import time


def carlo(L, d):
    cnt = 0
    while L > d:
        L -= random.uniform(0, L)
        cnt += 1
    return cnt


def solve(L, d):
    ret = []
    s = time.time()
    for i in range(2500000):
        ret.append(carlo(L, d))
    print(time.time() - s)
    print("{:.4f}".format(sum(ret) / len(ret)))


def solve2(L, d):
    if L <= d:
        print("{:.4f}".format(0))
        return
    dp = [0] * (10 * L + 1)
    pre_sum = 0
    for clen in range(10 * d + 1, 10 * L + 1):
        dp[clen] = (pre_sum / clen + 1) + (clen - d) / clen
        pre_sum += dp[clen]
    print("{:.4f}".format(dp[-1]))


if __name__ == '__main__':
    L, d = map(int, input().split())
    solve(L, d)
    # solve2(2, 1)
