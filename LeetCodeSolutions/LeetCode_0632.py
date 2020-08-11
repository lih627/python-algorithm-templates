class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        rmin, rmax = float('+inf'), float('-inf')
        import heapq
        heap = []
        for idx, num in enumerate(nums):
            heapq.heappush(heap, [num[0], idx])
            rmin = min(num[0], rmin)
            rmax = max(num[0], rmax)
        idxs = [0] * len(nums)
        cmin, cmax = rmin, rmax
        while True:
            # print(heap)
            cmin, idx = heapq.heappop(heap)
            if cmax - cmin < rmax - rmin:
                rmax = cmax
                rmin = cmin
            idxs[idx] += 1
            if idxs[idx] == len(nums[idx]):
                break
            tmp = nums[idx][idxs[idx]]
            cmax = max(tmp, cmax)
            heapq.heappush(heap, [tmp, idx])
        return [rmin, rmax]
