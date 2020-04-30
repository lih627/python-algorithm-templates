"""
1. dict + random.choice
2. Reservoir Sampling
"""


class Solution:

    def __init__(self, nums: List[int]):
        from collections import defaultdict
        self.d = defaultdict(list)
        for idx, num in enumerate(nums):
            self.d[num].append(idx)

    def pick(self, target: int) -> int:
        import random
        return random.choice(self.d[target])


class Solution2:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        cnt = 0
        import random
        for idx, num in enumerate(self.nums):
            if num == target:
                if cnt == 0:
                    pick = idx
                    cnt += 1
                else:
                    cnt += 1
                    if random.randint(1, cnt) > cnt - 1:
                        pick = idx
        return pick

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
