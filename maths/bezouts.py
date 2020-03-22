"""
LeetCode_365 水壶问题
有两个容量分别为 x 升 和 y 升 的水壶以及无限多的水。
请判断能否通过使用这两个水壶，从而可以得到恰好 z 升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z 升 水。
"""

import math


def canMeasureWater(x: int, y: int, z: int) -> bool:
    if x + y < z:
        return False
    if x == 0 or y == 0:
        return z == 0 or x + y == z
    return z % math.gcd(x, y) == 0
