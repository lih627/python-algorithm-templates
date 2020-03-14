class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for idx, _ in enumerate(nums):
            for j in range(idx + 1, n):
                if nums[j] > _:
                    dp[j] = max(dp[j], dp[idx] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        '''
        binary search solution
        '''
        if not nums:
            return 0
        cell = []

        for num in nums:
            if not cell or num > cell[-1]:
                cell.append(num)
                continue
            i, j = 0, len(cell)
            while i < j:
                mid = (i + j) // 2
                if cell[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            cell[i] = num
        return len(cell)
