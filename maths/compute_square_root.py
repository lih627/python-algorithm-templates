'''
Method of Compute Square Roots
1. Pocket calculators
2. binary search
3. Newton's method
'''

import math


def pocket_calculator(x):
    '''
    Pocket calculatros:
        \sqrt(x) = exp(1/2 * log (x))
    return sqrt(n)
    '''
    res = math.e ** (0.5 * math.log(x))
    return res


def binary_search(x: int) -> int:
    '''
    if x >= 2:
        0 < sqrt(x) < x / 2
    '''
    if x < 2:
        return x
    left, right = 2, x // 2
    while left <= right:
        pivot = left + (right - left) // 2
        num = pivot * pivot
        if num > x:
            right = pivot - 1
        elif num < x:
            left = pivot + 1
        else:
            return pivot
    return right


def newton_method(a: int):
    '''
    f(x) = x ** 2 - a = 0
    d(fx)/dx = 2 * x
    (x0, f(x0)): 2 * x0
    x_k = x_{k-1} - (x_{k-1}^2 -a)/(2*x_{k-1})
        = (x_{k + 1} + a / x_{k + 1}) / 2
    '''
    if a < 2:
        return a
    cur = a
    while True:
        pre = cur
        cur = (cur + a / cur) / 2
        if abs(pre - cur) < 1e-6:
            return cur


if __name__ == '__main__':
    n = 5
    print(pocket_calculator(n))
    print(binary_search(n))
    print(newton_method(n))
