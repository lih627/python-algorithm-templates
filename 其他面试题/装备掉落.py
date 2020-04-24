"""
打怪, 必掉1 件装备
a 0.8, b 0.2
问获得 ab 的期望
"""
import random
import numpy as np


def solve():
    for k in range(10):
        res = []
        for i in range(100000):
            cnt = 0
            ab = [0, 0]
            while True:
                cnt += 1
                if random.random() > 0.2:
                    ab[0] = 1
                else:
                    ab[1] = 1
                if sum(ab) == 2:
                    break
            res.append(cnt)
        print(np.mean(res))


if __name__ == '__main__':
    res = solve()
