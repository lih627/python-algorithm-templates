class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        maxn = [0] * T
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)
        last = pre = ret = 0
        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last
        return ret
