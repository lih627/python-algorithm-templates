import random


def fpowx(x, n):
    """
    quick pow: x ** n
    """
    res = 1
    while n:
        if n & 1:
            res = res * x
        # compute x^2 x^4 x^8
        x *= x
        n >>= 1
    return res


def fmulti(m, n, mod=10 ** 9 + 7):
    """
    并没有提速的效果
    只是对于其他语言 如c
    防止溢出
    对 python 没有任何帮助
    """
    res = 0
    while n:
        if n & 1:
            res += m
        m = (m + m) % mod
        res %= mod
        n >>= 1
    return res


def matrix_multiply(matrix_a, matrix_b):
    # 模 MOD 乘法/加法
    MOD = 10 ** 9 + 7
    n_row = len(matrix_a)
    n_col = len(matrix_b[0])
    n_tmp = len(matrix_a[0])
    matrix_c = [[0 for _ in range(n_col)] for _ in range(n_row)]
    for i in range(n_row):
        for j in range(n_col):
            for k in range(n_tmp):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j] % MOD
                matrix_c[i][j] %= MOD
    return matrix_c


def get_unit_matrix(n):
    # matrix I
    unit_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(n):
        unit_matrix[_][_] = 1
    return unit_matrix


def quick_matrix_pow(matrix_a, n):
    # A ^ n
    l = len(matrix_a)
    res = get_unit_matrix(l)
    while n:
        if n & 1:
            res = matrix_multiply(res, matrix_a)
        a = matrix_multiply(a, a)
        n >>= 1
    return res


def test_fmulti():
    m = random.randint(10 ** 9, 10 ** 15)
    n = random.randint(10 ** 9, 10 ** 15)
    res = fmulti(m, n)
    return res


def multi(m, n, mod=10 ** 9 + 7):
    return m * n % mod


def test_multi():
    m = random.randint(10 ** 9, 10 ** 15)
    n = random.randint(10 ** 9, 10 ** 15)
    res = multi(m, n)
    return res


if __name__ == '__main__':
    print('fast pow: 2 ** 11: {}'.format(fpowx(2, 11)))
    print(fmulti(987654, 987654321))
    print(987654 * 987654321 % (10 ** 9 + 7))

    # test the speed of fast(?)-multi
    import timeit

    T_fmulti = timeit.Timer('test_fmulti()',
                            'from __main__ import test_fmulti')
    print('f_multi: {:.6f}s'.format(T_fmulti.timeit(number=1000)))
    T_multi = timeit.Timer('test_multi()',
                           'from __main__ import test_multi')
    print('s_multi: {:.6f}s'.format(T_multi.timeit(number=1000)))

    # test matrix multiply
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 2], [3, 4], [5, 6]]
    c = matrix_multiply(a, b)
    print("a = {}\nb = {}\nc = {}".format(a, b, c))
