class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
        if k == 1:
            return nums
        from collections import deque
        que = deque()

        def _push(idx):
            if not que:
                que.append(idx)
            else:
                while que and nums[idx] >= nums[que[0]]:
                    que.popleft()
                while que and nums[idx] >= nums[que[-1]]:
                    que.pop()
                que.append(idx)

        for idx in range(k):
            _push(idx)
        res = [nums[que[0]]]
        for idx in range(k, n):
            if que[0] == idx - k:
                que.popleft()
            _push(idx)
            res.append(nums[que[0]])
        return res
