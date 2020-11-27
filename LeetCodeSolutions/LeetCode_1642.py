import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        pos = 0
        csum = 0
        while pos < len(heights):
            if pos == len(heights) - 1:
                return pos
            if heights[pos] >= heights[pos + 1]:
                pos += 1
                continue
            d = heights[pos + 1] - heights[pos]
            heapq.heappush(heap, -d)
            if csum + d <= bricks:
                csum += d
                pos += 1
            else:
                if ladders == 0:
                    return pos
                csum += d
                s = -heapq.heappop(heap)
                csum -= s
                ladders -= 1
                pos += 1
