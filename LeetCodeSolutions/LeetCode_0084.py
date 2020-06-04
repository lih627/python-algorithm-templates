class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        r = [0] * n
        l = [0] * n
        stack = []
        for idx, val in enumerate(heights):
            if idx == 0:
                stack.append(idx)
                continue
            while stack and val < heights[stack[-1]]:
                tmp = stack.pop()
                r[tmp] = idx
            stack.append(idx)
        while stack:
            tmp = stack.pop()
            r[tmp] = n

        for idx, val in enumerate(heights[::-1]):
            idx = n - 1 - idx
            if idx == n - 1:
                stack.append(idx)
                continue
            while stack and val < heights[stack[-1]]:
                tmp = stack.pop()
                l[tmp] = idx
            stack.append(idx)
        while stack:
            tmp = stack.pop()
            l[tmp] = - 1

        ans = 0
        for idx, val in enumerate(heights):
            ans = max(val * (r[idx] - l[idx] - 1), ans)
        return ans
