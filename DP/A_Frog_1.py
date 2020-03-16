def min_cost(n, heights):
    inf = 1e9
    if n == 1:
        return 0
    dp = [inf] * n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(heights[i] - heights[i - 1]),
                    dp[i - 2] + abs(heights[i] - heights[i - 2]))
    return dp[-1]


if __name__ == '__main__':
    n = int(input())
    heights = [int(_) for _ in input().split()]
    print(min_cost(n, heights))
