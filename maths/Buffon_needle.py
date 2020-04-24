import random


def buffon_needle(l, t, N=100000):
    def _sample_sine():
        r2 = 2
        while r2 > 1:
            u_1 = random.uniform(0, 1)
            u_2 = random.uniform(0, 1)
            v_1 = 2 * u_1 - 1
            r2 = v_1 ** 2 + u_2 ** 2
        return abs(2 * v_1 * u_2) / r2

    cnt = 0
    for _ in range(N):
        center = random.uniform(0, t / 2)
        sine = _sample_sine()
        if center < l * sine / 2:
            cnt += 1
    p = cnt / N
    print("P: {:.5f}, Pi:{:.10f}".format(p, 2 * l / (p * t)))


if __name__ == '__main__':
    for i in range(10):
        buffon_needle(1, 2)
