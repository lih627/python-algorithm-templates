'''
排序算法汇总:
bucket sort 桶排序

插入排序 insertion:
1. insertion sort 直接插入排序 stable
2. shell sort 希尔排序/分组插入排序 unstable

选择排序 selection:
1. selection sort 简单选择排序 unstable
2. heap sort 堆排序 unstable

交换排序 swap:
1. bubble sort 冒泡排序 stable
2. quick sort 快排 unstable

归并排序 merge sort
'''


def bucket_sort(nums):
    """
    O(n) 桶排序
    nums: List(int)
    """
    if not nums:
        return []
    buckets = [0] * (max(nums) - min(nums) + 1)
    for i in range(len(nums)):
        buckets[nums[i] - min(nums)] += 1
    res = []
    for i in range(len(buckets)):
        if buckets[i] != 0:
            res += [i + min(nums)] * buckets[i]
    return res


def bubble_sort_base(nums):
    """
    Bubble sort or sinking sort
    swapping algorithm
    Time complexity O(n^2)
    Space complexity O(1)
    Stable sort algorithm
    冒泡法 稳定排序
    """
    if not nums:
        return []
    n = len(nums)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def bubble_sort(nums):
    """
    Optimized bubble sort algorithm
    swapping algorithm
    O(n^2)
    Stable sort algorithm
    introduce a flag to monitor whether elements are
    getting swapped inside the loop.
    引入变量监视是否发生交换
    """
    if not nums:
        return []
    n = len(nums)
    for i in range(n - 1, 0, -1):
        flag = True
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
        if flag:
            break
    return nums


def selection_sort(nums):
    """
    Selection sort
    O(n^2)
    auxiliary Space O(1)
    not stable:
    [(7), 2, 4, 5, 7, 1] ->[1, 2, 4, 5, 7, (7)]
    选择排序不稳定
    """
    if not nums:
        return []
    n = len(nums)
    for i in range(n):
        min_idx = i
        # find the index of min value
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # Swap the found minimum element with
        # the first element
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def insertion_sort(nums):
    """
    insertion sort / 直接插入排序
    O(n^2)
    auxiliary space O(1)
    stable
    直接插入排序 稳定
    """
    if not nums:
        return []
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j > -1 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def shell_sort(nums):
    """
    shell sort / 希尔排序 插入排序一种
    O(n^2)
    not stable
    分组插入排序
    """
    if not nums:
        return []
    n = len(nums)
    # start with a big gap, then reduce the gap
    gap = n // 2
    while gap:
        for i in range(gap, n):
            tmp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > tmp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = tmp
        gap //= 2
    return nums


def heap_sort(nums):
    '''
    heap sort 堆排序
    time complexity of heapify is O(logn)
    create and build heap is O(n)
    overall time complexity is O(nlogn)
    unstable
    '''

    if not nums:
        return []
    n = len(nums)
    # build max heap
    for i in range(n // 2, -1, -1):
        heapify(nums, n, i)

    # one by one extract elements
    for i in range(n - 1, 0, -1):
        # swap
        nums[i], nums[0] = nums[0], nums[i]
        # buile max heap
        heapify(nums, i, 0)
    return nums


def heapify(arr, n, i):
    '''
    heapify subtree rooted at index 1
    '''
    largest = i
    l = 2 * i + 1  # left = 2 * index + 1
    r = 2 * i + 2  # right = 2 * indx + 2
    # print(arr)
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


if __name__ == '__main__':
    nums = [1, 3, 2, 4, 7, 6, 5, 8]
    res = {}
    res['bucket'] = bucket_sort(nums[:])
    res['bubble_base'] = bubble_sort_base(nums[:])
    res['bubble'] = bubble_sort(nums[:])
    res['selection'] = selection_sort(nums[:])
    res['shell'] = shell_sort(nums[:])
    res['heapsort'] = heap_sort(nums[:])

    for k, v in res.items():
        print('{}:{}'.format(k, v))
