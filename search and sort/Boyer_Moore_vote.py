from typing import List


def majorityElement(nums):
    '''
    The majority element is the element
    that appears more than ⌊ n/2 ⌋ times.
    '''
    count = 0
    candaidate = None
    for num in nums:
        if count == 0:
            candaidate = num
        count += 1 if num == candaidate else -1
    return candaidate


def majorityElement2(nums: List[int]) -> List[int]:
    '''
    Given an integer array of size n,
    find all elements that appear more
    than ⌊ n/3 ⌋ times.
    '''
    A = B = None
    cntA = cntB = 0
    for num in nums:
        if num == A:
            cntA += 1
            continue
        if num == B:
            cntB += 1
            continue
        if cntA == 0:
            A = num
            cntA += 1
            continue
        if cntB == 0:
            B = num
            cntB += 1
            continue
        cntA -= 1
        cntB -= 1
    cntA = nums.count(A) > len(nums) // 3
    cntB = nums.count(B) > len(nums) // 3
    res = []
    if cntA: res.append(A)
    if cntB: res.append(B)
    return res


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1, 2, 3, 4, 5]
    print(majorityElement(nums))
    nums = [1, 1, 2, 2, 3]
    print(majorityElement2(nums))
