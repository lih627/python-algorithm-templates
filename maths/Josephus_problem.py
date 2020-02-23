'''
Josephus problem
约瑟夫环
0,1,...,n-1 这 n 个数字排成一个圆圈，
从数字 0 开始，每次从这个圆圈里删除第 m 个数字。
求出这个圆圈里剩下的最后一个数字。
n >= 1
m >= 1

n = 5, m = 3 return 3
n = 10, m = 17 return 2
'''


def lastRemaining(n, m):
    '''
    f(1) = 0 只剩一个人当前轮标号为 0
    当前轮第0个坐标, 是上一轮的第m个坐标
    f(2) = (f(1) + m) mod 2
    当前轮的第0个坐标,是上一轮的第m个坐标
    当前轮的第k个坐标,是上一轮的的第 (m + k) mod 总人数 个坐标
    ...
    f(i) = (f(i -1) + m) mod i
    n = 4 m = 3 [下标]
    0 1 2 3 [0 1 2 3]
    3 0 1 [0 1 2]
    3 0 [0 1]
    0 [0]
    '''
    res = 0
    for i in range(2, n + 1):
        res = (res + m) % i
    return res


if __name__ == '__main__':
    print(lastRemaining(5, 3))
    print(lastRemaining(4, 3))
