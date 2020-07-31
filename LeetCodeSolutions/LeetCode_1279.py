from threading import Lock


class TrafficLight:
    def __init__(self):
        self.A = Lock()

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        if roadId == 1:
            if self.A.locked():
                self.A.release()
                turnGreen()
            crossCar()
        else:
            if not self.A.locked():
                self.A.acquire()
                turnGreen()

            crossCar()


#
# @lc app=leetcode.cn id=1279 lang=python3
#
# [1279] 红绿灯路口
#

# @lc code=start
class TrafficLight:
    def __init__(self):
        self.A = 1
        pass

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        if roadId == 1:
            if self.A == 0:
                self.A = 1
                turnGreen()
            crossCar()
        else:
            if self.A == 1:
                self.A = 0
                turnGreen()
            crossCar()

# @lc code=end
