import random

"""
测试一下不同parition时间差异
发现对于非极端用例,
并没有明显的时间差异
"""


def partition_fast(nums, low, high):
    x = nums[low]
    i = low

    for j in range(low + 1, high + 1):
        if nums[i] < x:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    nums[i], nums[low] = nums[low], nums[i]
    return i


def partition_slow(nums, low, high):
    x = nums[low]
    i = high + 1

    for j in range(high, low, -1):
        if nums[j] > x:
            i -= 1
            nums[i], nums[j] = nums[j], nums[i]
    i -= 1
    nums[i], nums[low] = nums[low], nums[i]
    return i


def quick_sort_fast(nums, low, high):
    if low < high:
        pivot = partition_fast(nums, low, high)
        quick_sort_fast(nums, low, pivot - 1)
        quick_sort_fast(nums, pivot + 1, high)


def quick_sort_slow(nums, low, high):
    if low < high:
        pivot = partition_slow(nums, low, high)
        quick_sort_slow(nums, low, pivot - 1)
        quick_sort_slow(nums, pivot + 1, high)


def random_list(start=0, stop=100, length=100):
    if length >= 0:
        length = int(length)
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def fast():
    nums = random_list()
    quick_sort_fast(nums, 0, len(nums) - 1)


def slow():
    nums = random_list()
    quick_sort_slow(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    from timeit import Timer

    t1 = Timer('fast()', 'from __main__ import fast')
    print('fast: {:.4f}s'.format(t1.timeit(number=1000)))
    t2 = Timer('slow()', 'from __main__ import slow')
    print('slow: {:.4f}s'.format(t2.timeit(number=1000)))
    t1 = Timer('fast()', 'from __main__ import fast')
    print('fast: {:.4f}s'.format(t1.timeit(number=1000)))
    t2 = Timer('slow()', 'from __main__ import slow')
    print('slow: {:.4f}s'.format(t2.timeit(number=1000)))
