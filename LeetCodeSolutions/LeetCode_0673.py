class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        length, cnt = [1] * n, [1] * n
        for idx, _ in enumerate(nums):
            for j in range(idx):
                if nums[j] < _:
                    if length[idx] == length[j]:
                        length[idx] += 1
                        cnt[idx] = cnt[j]
                    elif length[idx] == length[j] + 1:
                        cnt[idx] += cnt[j]
        longest = max(length)
        return sum([x[1] for x in enumerate(cnt) if length[x[0]] == longest])

        ''' 
        l = 1
        cnt = 0
        def helper(idx, tmp):
            nonlocal cnt, l
            if len(tmp) == l:
                cnt += 1
            elif len(tmp) > l:
                l = len(tmp)
                cnt = 1
            for i in range(idx, len(nums)):
                if tmp == []:
                    helper(i + 1, [nums[i]])
                else:
                    if nums[i] > tmp[-1]:
                        helper(i + 1, tmp + [nums[i]])
        helper(0, [])
        return cnt
        '''
