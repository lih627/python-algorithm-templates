class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.mins:
            self.mins.append(x)
        else:
            if x < self.mins[-1]:
                self.mins.append(x)
            else:
                self.mins.append(self.mins[-1])

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
