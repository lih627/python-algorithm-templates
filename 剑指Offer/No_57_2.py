class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        from collections import deque
        if target == 1:
            return []
        res = []
        tmp = deque()
        cur_sum = 0
        for i in range(1, target // 2 + 2):
            cur_sum += i
            tmp.append(i)
            while cur_sum > target:
                cur_sum -= tmp.popleft()
            if cur_sum == target:
                res.append(list(tmp))
        return res
