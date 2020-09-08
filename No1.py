def solve(n, nums):
    if len(set(nums)) == len(nums):
        print(0)
        return None
    left = [1] * len(nums)
    right = [1] * len(nums)
    for idx, val in enumerate(nums):
        if idx == 0:
            continue
        tmp = 1
        for i in range(idx):
            if val < nums[i]:
                tmp = max(tmp, 1 + left[i])
        left[idx] = tmp

    for idx, val in enumerate(nums[::-1]):
        if idx == 0:
            continue
        tmp = 1
        for i in range(idx):
            if val < nums[i]:
                tmp = max(tmp, 1 + right[i])
        right[idx] = tmp
    right = right[::-1]
    ret = 2
    for idx, val in enumerate(nums):
        for j in range(idx + 1, len(nums)):
            if nums[j] == val:
                ret = max(ret, 2 * min(left[idx], right[j]))
                break
    print(ret)


if __name__ == '__main__':
    T = int(input())
    n = []
    nums = []
    for _ in range(T):
        n.append(int(input()))
        nums.append(list(map(int, input().split())))
    for (n_, nums_) in zip(n, nums):
        solve(n_, nums_)
