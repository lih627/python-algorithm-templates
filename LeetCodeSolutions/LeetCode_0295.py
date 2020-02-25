class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_root_heap = []
        self.min_root_heap = []

    def addNum(self, num: int) -> None:
        import heapq
        if len(self.max_root_heap) == len(self.min_root_heap):
            tmp = heapq.heappushpop(self.max_root_heap, -num)
            heapq.heappush(self.min_root_heap, -tmp)
        else:
            cur_max = heapq.heappop(self.min_root_heap)
            print(cur_max, num)
            if cur_max < num:
                heapq.heappush(self.min_root_heap, num)
                heapq.heappush(self.max_root_heap, - cur_max)
            else:
                heapq.heappush(self.min_root_heap, cur_max)
                heapq.heappush(self.max_root_heap, -num)

    def findMedian(self) -> float:
        m = len(self.max_root_heap)
        n = len(self.min_root_heap)
        if m == n == 0:
            return None
        if m == n:
            return (-self.max_root_heap[0] + self.min_root_heap[0]) / 2
        else:
            return self.min_root_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
