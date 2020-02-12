"""
Catalan number: https://oi-wiki.org/math/catalan/

index   0   1   2   3   4   5   6 ...
value   1   1   2   5   14  42  132..

The basic version: catalan_base
H(n) = sum (i = 1 to n H(i - 1) * H(n - i))



          [2n]
          [ n]
H(n) =  --------- n >= 2
          n + 1

          H(n - 1) * (4 * n - 2)
H(n) = --------------------------
           n + 1

       [ 2n]   [ 2n]
H(n) = [   ] - [   ]
       [  n]   [n-1]


"""


def catalan_base(n):
    """
    base case
    H(n) = sum (i = 1 to n H(i - 1) * H(n - i))
    """
    if n < 2:
        return 1
    res = 0
    for i in range(n):
        res += catalan_base(i) * catalan_base(n - i - 1)
    return res


def catalan_dp(n):
    """
    dynamic programming based function
    O(n**2)
    """
    if n < 2:
        return 1
    catalan = [0 for _ in range(n + 1)]
    catalan[0], catalan[1] = 1, 1
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i - j - 1]
    return catalan[n]


def catalan_binomial_coefficient(n):
    """
    The most fast version
    O(n): H(n) = C(2n, n) / (n + 1)
    wiki: https://en.wikipedia.org/wiki/Binomial_coefficient
                  n!
    C(n, k) = ----------
               k!(n-k)!
                                n + 1 - i
            = for i = 1 to k: -------------
                                    i
    """

    def binomialCofficient(n, k):
        # C(n, k ) = C(n, n - k)
        if k > n - k:
            k = n - k
        res = 1
        for i in range(k):
            res *= n - i
            res /= i + 1
        return res

    c = binomialCofficient(2 * n, n)
    return c // (n + 1)


def catalan_factorial(n):
    """
    O(n): H(n) = C(2n, n) / (n + 1)
    """
    import math
    a = math.factorial(2 * n)
    b = math.factorial(n)
    return a // b // b // (n + 1)


if __name__ == '__main__':
    funcs = [catalan_base, catalan_dp,
             catalan_binomial_coefficient, catalan_factorial]
    import time

    '''
func:catalan_base, time:173.4288, res: [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190]
func:catalan_dp, time:0.0003, res: [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190]
func:catalan_binomial_coefficient, time:0.0000, res: [1, 1.0, 2.0, 5.0, 14.0, 42.0, 132.0, 429.0, 1430.0, 4862.0, 16796.0, 58786.0, 208012.0, 742900.0, 2674440.0, 9694845.0, 35357670.0, 129644790.0, 477638700.0, 1767263190.0]
func:catalan, time:0.0038, res: [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190]

    '''
    for func in funcs:
        res = []
        start = time.time()
        for i in range(20):
            res.append(func(i))
        print('func:{}, time:{:.4f}, res: {}'.format(func.__name__,
                                                     time.time() - start,
                                                     res))
