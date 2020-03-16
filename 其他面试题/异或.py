"""
给定整数m以及n个数字A1, A2, …, An，
将数列A中所有元素两两异或，
共能得到n(n-1)/2个结果。
请求出这些结果中大于m的有多少个。
"""


class TireNode:
    def __init__(self):
        self.children = [None] * 2
        self.cnt = 0


class TireTree:

    def __init__(self):
        self.root = TireNode()

    def insert(self, num, level=31):
        pre = self.root
        while level > -1:
            idx = 1 & (num >> level)
            if not pre.children[idx]:
                pre.children[idx] = TireNode()
            pre.children[idx].cnt += 1
            pre = pre.children[idx]
            level -= 1

    def query(self, m, num, level=31):
        res = 0
        pre = self.root
        while level > -1 and pre:
            digit_m = 1 & (m >> level)
            digit_n = 1 & (num >> level)
            if digit_m == 0 and digit_n == 1:
                if pre.children[0]:
                    res += pre.children[0].cnt
                pre = pre.children[1]
            elif digit_m == 1 and digit_n == 0:
                pre = pre.children[1]
            elif digit_m == 0 and digit_n == 0:
                if pre.children[1]:
                    res += pre.children[1].cnt
                pre = pre.children[0]
            else:
                pre = pre.children[0]
            level -= 1
        return res

    def __repr__(self):
        pass


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    l = len(bin(max(nums))) - 3
    res = 0
    tire_tree = TireTree()
    for num in nums:
        tire_tree.insert(num, l)
    res = 0
    for num in nums:
        res += tire_tree.query(m, num, l)
    print(res // 2)
