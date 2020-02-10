class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for _ in nums:
            if _ in res:
                return True
            res.add(_)
        return False
