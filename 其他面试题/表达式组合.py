"""
给定一个字符串"123456789"
在任意字符中间插入 + - * / 四种运算符
使最火的计算结果等于 50
例如 1*2*3*4-56-7+89 = 50
输出所有可能的表达式
"""

import itertools


def make_50():
    nums = [str(_) for _ in range(1, 10)]
    ops = ['+', '-', '*', '//', '']
    for op in itertools.product(*([ops for _ in range(8)])):
        cur = ''.join([op[i // 2] if i & 1 else nums[i // 2] for i in range(17)])
        if eval(cur) == 50:
            print(cur)


if __name__ == '__main__':
    make_50()
