"""
https://blog.csdn.net/noahzuo/article/details/52037151
"""


def checkOverlap(radius: int, x_center: int,
                 y_center: int, x1: int, y1: int,
                 x2: int, y2: int) -> bool:
    # 计算矩形中心点, 宽和高
    x_c = (x1 + x2) / 2
    y_c = (y1 + y2) / 2
    w = x2 - x1
    h = y2 - y1
    # 平移矩形到坐标系原点, 记录矩形中心与右上顶点构成的向量OA
    OA = [x2 - x_c, y2 - y_c]
    # 平移矩形的时候, 平移圆
    x_center -= x_c
    y_center -= y_c
    # 通过对称, 将圆心放到第一象限
    x_center = abs(x_center)
    y_center = abs(y_center)
    # 记录坐标原点到圆心的向量 OB
    OB = [x_center, y_center]
    # 计算向量AB:
    AB = [OB[0] - OA[0], OB[1] - OA[1]]
    # 计算向量AC, C是将AB中的负值置0
    AC = [max(0, AB[0]), max(0, AB[1])]
    # print(AC)
    return AC[0] ** 2 + AC[1] ** 2 <= radius ** 2
