class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        ret = (D - B) * (C - A) + (H - F) * (G - E)
        x1, y1, x2, y2 = max(A, E), max(B, F), min(C, G), min(D, H)
        overlap = max(0, y2 - y1) * max(0, x2 - x1)
        # print(ret, overlap)
        return ret - overlap
