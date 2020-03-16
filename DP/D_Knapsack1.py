n, w = map(int, input().split())
elems = []
for _ in range(n):
    elems.append(list(map(int, input().split())))
res = [0] * (w + 1)
for item in elems:
    for j in range(w, item[0] - 1, -1):
        res[j] = max(res[j], res[j - item[0]] + item[1])

print(res[-1])
