class MaxQueue:

    def __init__(self):
        self.que = collections.deque()
        self.max_que = collections.deque()

    def max_value(self) -> int:
        if self.que:
            return self.max_que[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.que.append(value)
        while self.max_que and value > self.max_que[-1]:
            self.max_que.pop()
        self.max_que.append(value)

    def pop_front(self) -> int:
        if self.que:
            if self.que[0] == self.max_que[0]:
                self.max_que.popleft()
            return self.que.popleft()
        else:
            return -1

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
