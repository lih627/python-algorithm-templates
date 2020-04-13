"""
欧几里得算法/ 辗转相除法

gcd(a, b) = gcd(a, a mod b)
"""


# def gcd(a, b):
#     if b == 0:
#         return a
#     if a % b:
#         return gcd(b, a % b)
#     return b

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == '__main__':
    print(gcd(2, 5))
    print(gcd(10, 0))
    print(gcd(2, 4))

