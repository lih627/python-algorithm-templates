class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        for r in regions[::-1]:
            if region1 in r:
                region1 = r[0]
            if region2 in r:
                region2 = r[0]
            if region1 == region2:
                return region1
