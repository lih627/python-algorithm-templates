"""
打车派单场景 , 假定有 N 个订单， 待分配给 N 个司机。
每个订单在匹配司机前，会对候选司机进行打分，打分的结果保存在 N*N 的矩阵 A，
其中 Aij 代表订单 i 司机 j 匹配的分值。

假定每个订单只能派给一位司机，
司机只能分配到一个订单。求最终的派单结果，
使得匹配的订单和司机的分值累加起来最大，
并且所有订单得到分配。

题目链接 http://dwz.date/R6Z
"""


def backtrack(n, scores):
    used = [False] * n
    used = tuple(used)
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def helper(index, used):
        tpath = []
        tscore = float('-inf')
        if index == n:
            tscore = 0
        for i in range(n - 1, -1, -1):
            if not used[i]:
                used = list(used)
                used[i] = True
                used = tuple(used)
                a = helper(index + 1, used)
                if tscore <= a[1] + scores[index][i]:
                    tscore = a[1] + scores[index][i]
                    tpath = [(index, i)] + a[0]
                used = list(used)
                used[i] = False
                used = tuple(used)
        return (tpath, tscore)

    ret = helper(0, used)
    print('{:.2f}'.format(ret[1]))
    for tmp in ret[0]:
        print("{} {}".format(tmp[0] + 1, tmp[1] + 1))


if __name__ == '__main__':
    n = int(input())
    scores = []
    for _ in range(n):
        scores.append(list(map(float, input().split())))
    backtrack(n, scores)
