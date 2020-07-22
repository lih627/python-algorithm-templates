from collections import defaultdict


def solve(a, n, m):
    cnt = defaultdict(int)
    ret = 0
    for idx, val in enumerate(a):
        cnt[val] += 1;
        if cnt[val] == m:
            ret += n - idx
            cnt[val] -= 1
            # print(idx, ret, cnt)
    return ret


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    print(solve(a, n, m))
