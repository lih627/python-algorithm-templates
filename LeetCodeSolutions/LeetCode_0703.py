import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxRoot = []
        self.minRoot = []
        for num in nums:
            heapq.heappush(self.minRoot, num)
        while len(self.minRoot) > k - 1:
            heapq.heappush(self.maxRoot, -heapq.heappop(self.minRoot))

    def add(self, val: int) -> int:
        heapq.heappush(self.minRoot, val)
        heapq.heappush(self.maxRoot, -heapq.heappop(self.minRoot))
        return -self.maxRoot[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
