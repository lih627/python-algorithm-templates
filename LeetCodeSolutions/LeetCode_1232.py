class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        p0, p1 = coordinates[0], coordinates[1]

        def helper(p):
            return (p[0] - p0[0]) * (p1[1] - p0[1]) == (p[1] - p0[1]) * (p1[0] - p0[0])

        for p in coordinates[2:]:
            if not helper(p):
                return False
        return True
