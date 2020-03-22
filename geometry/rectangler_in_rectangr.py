"""
https://stackoverflow.com/questions/13784274/detect-if-one-rect-can-be-put-into-another-rect
detect-if-one-rect-can-be-put-into-another-rect


See Rectangles in Rectangles for more details
"""


def pq_in_ab(a, b, p, q):
    a, b = max(a, b), min(a, b)
    p, q = max(p, q), min(p, q)
    return p <= a and q <= b or (p > a and (p ** 2 + q ** 2) * b >=
                                 2 * p * q * a + (p ** 2 - q ** 2) *
                                 (q ** 2 + p ** 2 - a ** 2) ** 0.5)
