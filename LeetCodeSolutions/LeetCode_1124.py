class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        wpi = [0]
        for h in hours:
            if h > 8:
                wpi.append(1)
            else:
                wpi.append(-1)
        for idx, val in enumerate(wpi):
            if idx == 0:
                continue
            else:
                wpi[idx] += wpi[idx - 1]
        stack = []
        for idx, val in enumerate(wpi):
            if not stack or stack[-1][0] > val:
                stack.append([val, idx])
        n = len(wpi)
        ans = 0
        for i in range(n - 1, -1, -1):
            if stack and i == stack[-1][1]:
                stack.pop()
            while stack and wpi[i] - stack[-1][0] > 0:
                ans = max(ans, i - stack[-1][1])
                stack.pop()
        return ans
