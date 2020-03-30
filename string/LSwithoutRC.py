"""
The longest substring without repeating characters.
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring,
              "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s: str) -> int:
    """
    滑动窗口法
    """
    if not s:
        return 0
    d = {}
    left = 0
    res = 0
    for right, val in enumerate(s):
        if val in d:
            left = max(left, d[val] + 1)
        d[val] = right
        res = max(res, d[val] - left + 1)
    return res
