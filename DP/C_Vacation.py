n = int(input())
h = []
for _ in range(n):
    h.append(list(map(int, input().split())))

res = h[0]
for i in range(1, n):
    tmp = res[:]
    for j in range(3):
        res[j] = h[i][j] + max(tmp[(j + 1) % 3], tmp[j - 1])
print(max(res))
