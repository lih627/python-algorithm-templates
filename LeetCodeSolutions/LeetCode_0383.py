class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        for k in cnt1:
            if k not in cnt2 or cnt1[k] > cnt2[k]:
                return False
        return True
