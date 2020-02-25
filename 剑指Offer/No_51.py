class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_count(nums):
            if len(nums) < 2:
                return 0, nums
            mid = len(nums) // 2
            lcnt, left = merge_count(nums[:mid])
            rcnt, right = merge_count(nums[mid:])
            cnt = lcnt + rcnt
            l = r = 0
            res = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    # left数组剩余的数都大于right数组当前的这个数
                    # 构成 len(left) - l 个逆序对
                    cnt += len(left) - l
                    r += 1
            return cnt, res + left[l:] + right[r:]

        res, tmp = merge_count(nums)
        return res
