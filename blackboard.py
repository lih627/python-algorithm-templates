from collections import defaultdict


def solve(n=1000):
    t = set([2])
    f = set([1, 3])
    for i in range(4, n + 1):
        j = 1
        isT = False
        while j < i // 2 + 1:
            if i % j == 0 and i - j in f:
                t.add(i)
                isT = True
                break
            j += 1
        if not isT:
            f.add(i)
    print(list(t))
    print(list(f))
    return t

if __name__ == '__main__':
    solve()
