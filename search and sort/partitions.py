"""
总结不同的partition用法
"""
import random


def partition_base(arr, low, high):
    '''
    基础的思路, 以高位元素作为pivot元素
    一次遍历
    对于接近排序数组, 时间复杂度退化
    '''
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def partition_2_pointer(arr, low, high):
    '''
    双指针遍历,
    对于有重复元素的数组, 重复元素等概率在pivot两侧
    '''
    x = arr[low]
    i, j = low, high
    while i <= j:
        while i <= j and arr[i] <= x:
            i += 1
        while j >= i and arr[j] >= x:
            # j 始终指的元素比x小
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[low] = arr[low], arr[j]
    return j


def partition_random(arr, low, high):
    '''
    随机初始化pivot
    对于接近排序数组效果较好
    '''
    # random_idx in [low, high]
    random_idx = random.randint(low, high)
    arr[low], arr[random_idx] = arr[random_idx], arr[low]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
