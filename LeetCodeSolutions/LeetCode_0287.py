class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # fast slow pointer
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        res = 0
        while True:
            res = nums[res]
            slow = nums[slow]
            if res == slow:
                return res
