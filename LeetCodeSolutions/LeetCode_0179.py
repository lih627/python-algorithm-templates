from functools import cmp_to_key


def _cmp(a, b):
    ab = a + b
    ba = b + a
    if ab < ba:
        return -1
    elif ab == ba:
        return 0
    else:
        return 1


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        ret = sorted(str_nums, key=cmp_to_key(_cmp), reverse=True)
        return ''.join(ret)
