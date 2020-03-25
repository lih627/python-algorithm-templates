"""
360公司 2020笔试题
有一种特殊的DNA, 仅仅由 A 和 T 组成, 顺次链接

科学家通过一种手段, 可以改变这种DNA, 每一次, 科学家可以交换改DNA上的
两个核酸的位置, 也可以把特定位置的某个核酸修改为另外一种.

有一个DNA 希望改造成另外一个DNA, 计算最小操作次数

输入
ATTTAA
TTAATT
返回 3
"""


def solve(s1, s2):
    """
    找规律题, 先通过更改核酸, 让两个核酸的A和T数量一致,
    注意修改后的核酸放到正确位置上
    然后对不满足要求的位置记录其更换次数
    更换次数 等于 总不满足要求的位置个数 // 2
    """
    from collections import Counter
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    s1 = list(s1)
    s2 = list(s2)
    res = 0
    a_num = counter1['A'] - counter2['A']
    res += abs(a_num)
    A2T = True if a_num < 0 else False
    if a_num != 0:
        cnt = abs(a_num)
        if A2T:
            for i in range(len(s1)):
                if s1[i] == 'T' and s2[i] == 'A':
                    s2[i] = 'T'
                    cnt -= 1
                if cnt == 0:
                    break
        else:
            for i in range(len(s1)):
                if s1[i] == 'A' and s2[i] == 'T':
                    s2[i] = 'A'
                    cnt -= 1
                if cnt == 0:
                    break
    for i in range(len(s1)):
        if s1[i] == 'A' and s2[i] == 'T':
            res += 1
    return res


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(solve(s1, s2))
