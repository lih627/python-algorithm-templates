if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        v = set()
        ret = False
        n = int(input())
        for i in range(n):
            cur = tuple(sorted(map(int, input().split())))
            if cur in v:
                ret = True
            v.add(cur)
        print('YES' if ret else 'NO')
