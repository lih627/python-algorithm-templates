"""
sieve of Eratosthenes
埃氏筛
"""


def countPrimes(n: int) -> int:
    if n < 2: return 0
    res = [1] * n
    res[0], res[1] = 0, 0
    for i in range(2, int(n ** 0.5) + 1):
        # print(res)
        if res[i]:
            res[i * i: n: i] = [0] * len(res[i * i: n: i])
    return sum(res)
