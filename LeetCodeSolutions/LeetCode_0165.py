class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(max(len(v1), len(v2))):
            try:
                s1 = int(v1[i])
            except:
                s1 = 0
            try:
                s2 = int(v2[i])
            except:
                s2 = 0
            if s1 < s2:
                return -1
            elif s1 > s2:
                return 1
        return 0
