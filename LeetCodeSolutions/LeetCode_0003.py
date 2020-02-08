class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        cnt = 0
        sldwin = []
        for idx, v in enumerate(s):
            if v not in sldwin:
                sldwin.append(v)
            else:
                i = sldwin.index(v)
                cnt = len(sldwin) if len(sldwin) > cnt else cnt
                sldwin.append(v)
                sldwin = sldwin[i + 1:]
        cnt = len(sldwin) if len(sldwin) > cnt else cnt
        return cnt
