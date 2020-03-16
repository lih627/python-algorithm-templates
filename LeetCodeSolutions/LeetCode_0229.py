class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        A = B = None
        cntA = cntB = 0
        for num in nums:
            if num == A:
                cntA += 1
                continue
            if num == B:
                cntB += 1
                continue
            if cntA == 0:
                A = num
                cntA += 1
                continue
            if cntB == 0:
                B = num
                cntB += 1
                continue
            cntA -= 1
            cntB -= 1
        cntA = nums.count(A) > len(nums) // 3
        cntB = nums.count(B) > len(nums) // 3
        res = []
        if cntA: res.append(A)
        if cntB: res.append(B)
        return res
