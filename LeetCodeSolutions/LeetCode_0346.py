import collections


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.stack = collections.deque()
        self.sum = 0
        self.size = size

    def next(self, val: int) -> float:
        if len(self.stack) < self.size:
            self.stack.append(val)
            self.sum += val
            return self.sum / len(self.stack)
        else:
            self.sum -= self.stack.popleft()
            self.sum += val
            self.stack.append(val)
            return self.sum / len(self.stack)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
