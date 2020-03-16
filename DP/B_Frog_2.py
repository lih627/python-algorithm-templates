n, k = [int(_) for _ in input().split()]
h = [int(_) for _ in input().split()]
inf = 1e9
dp = [inf] * n
dp[0] = 0
for i in range(1, n):
    cnt = 1
    while cnt <= k and i - cnt > -1:
        dp[i] = min(dp[i], dp[i - cnt] + abs(h[i] - h[i - cnt]))
        cnt += 1
print(dp[-1])
