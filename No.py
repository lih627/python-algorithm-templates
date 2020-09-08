from collections import defaultdict


def upper_bound(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return l


def solve(nums):
    d = defaultdict(list)
    for idx, val in enumerate(nums):
        d[val].append(idx)
    hunderds, ten, one = 9, 9, 9
    while hunderds > -1:
        if len(d[hunderds]) >= 3:
            return hunderds * 100 + hunderds * 10 + hunderds * 1
        elif len(d[hunderds]) == 0:
            hunderds -= 1
        else:
            hpos = d[hunderds][0]
            ten = 9
            while ten > -1:
                tidx = upper_bound(d[ten], hpos)
                if tidx == len(d[ten]):
                    ten -= 1
                    continue
                tpos = d[ten][tidx]
                one = 9
                while one > -1:
                    oidx = upper_bound(d[one], tpos)
                    if oidx == len(d[one]):
                        one -= 1
                        continue
                    return hunderds * 100 + ten * 10 + one
                ten -= 1
            hunderds -= 1


if __name__ == '__main__':
    nums = [0, 0, 0]
    print(solve(nums))
