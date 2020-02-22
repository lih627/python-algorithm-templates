class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Set = set()
        left, right, longest = 0, 0, 0
        while right < len(s):
            while s[right] in Set:
                Set.remove(s[left])
                left += 1
            Set.add(s[right])
            right += 1
            longest = max(right - left, longest)
        return longest
