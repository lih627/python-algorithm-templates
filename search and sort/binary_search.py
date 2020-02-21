def binary_search_base(nums: list, target: int) -> int:
    """
    Time complexi O(logn)
    The basic binary search
    nums is a sorted list
    if multi targets in nums, return one target index
    else return -1
    """
    if not nums:
        return -1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return -1


def lower_bound(nums: list, target: int) -> int:
    '''
    return the target lower bound index in nums
    c++ algorithms
    '''
    first, last = 0, len(nums)
    while first < last:
        mid = first + (last - first) // 2
        if nums[mid] < target:
            first = mid + 1
        else:
            last = mid
    return first


def upper_bound(nums: list, target: int) -> int:
    '''
    return the first idx in nums when nums[idx] > target
    '''
    first, last = 0, len(nums)
    while first < last:
        mid = first + (last - first) // 2
        if nums[mid] <= target:
            first = mid + 1
        else:
            last = mid
    return first


def left_bound(nums: list, target: int) -> int:
    '''
    return the target left_bound index in nums
    if target not in nums, return -1
    e.g.,
    nums = [1, 2, 2, 3, 3, 3, 4], target = 2
    return 1
    '''
    if not nums:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    if -1 < left < len(nums) and nums[left] == target:
        return left
    return -1


def right_bound(nums: list, target: int) -> int:
    '''
        return the target left_bound index in nums
        if target not in nums, return -1
        e.g.,
        nums = [1, 2, 2, 3, 3, 3, 4], target = 2
        return 2
        '''
    if not nums:
        return -1
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        res = left - 1
    if -1 < res < len(nums) and nums[res] == target:
        return res
    return -1


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 3, 3, 4, 5, 6]
    target = 3
    print(binary_search_base(nums, target))
    print(left_bound(nums, target))
    print(right_bound(nums, target))
    print(lower_bound(nums, target))
    print(upper_bound(nums, target))
