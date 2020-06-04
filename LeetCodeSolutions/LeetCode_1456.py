class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set(list("aeiou"))
        cnt = 0
        l, r = 0, k - 1;
        cur = 0
        for i in range(l, r + 1):
            if s[i] in vowel:
                cur += 1
        cnt = max(cur, cnt)
        while r < len(s) - 1:
            # print(l, r)
            r += 1
            if s[r] in vowel:
                cur += 1
            if s[l] in vowel:
                cur -= 1
            l += 1
            if cur > cnt:
                cnt = cur
        return cnt
