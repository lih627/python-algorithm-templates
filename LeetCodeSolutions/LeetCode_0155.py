class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min:
            self.min.append(x)
        else:
            if self.min[-1] < x:
                self.min.append(self.min[-1])
            else:
                self.min.append(x)

    def pop(self) -> None:
        if not self.stack:
            return
        else:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min:
            return
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
