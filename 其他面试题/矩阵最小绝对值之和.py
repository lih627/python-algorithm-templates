"""
阿里 2020 笔试

给定一个数组 n，比如
5 10 5 4 4
1  7  8 4 0
3  4  9 0 3
从每一列选择一个数，求出后一列减去前一列的绝对值的和的最小值
比如这里就是 5 7 5 4 4，所以输出是 5
"""


def solve(n, nums):
    """
    当前节点的最优值: 当前节点的值, 减去前三个节点的值, 取abs, 加上
    前三个节点保存的最优值, 取最小
    """
    pre = [0] * 3
    nums = list(zip(nums[0], nums[1], nums[2]))
    for i in range(1, n):
        cur = [0, 0, 0]
        for j in range(3):
            cur[j] = min(
                abs(nums[i][j] - nums[i - 1][0]) + pre[0],
                abs(nums[i][j] - nums[i - 1][1]) + pre[1],
                abs(nums[i][j] - nums[i - 1][2]) + pre[2]
            )
        pre = cur
    return min(pre)


if __name__ == '__main__':
    n = int(input())
    res = []
    for i in range(3):
        res.append(list(map(int, input().split())))
    print(solve(n, res))
