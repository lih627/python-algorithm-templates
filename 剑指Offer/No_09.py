class CQueue:

    def __init__(self):
        self.addstack = []
        self.deletestack = []

    def appendTail(self, value: int) -> None:
        self.addstack.append(value)

    def deleteHead(self) -> int:
        if self.deletestack:
            return self.deletestack.pop()
        else:
            while self.addstack:
                self.deletestack.append(self.addstack.pop())
            if self.deletestack:
                return self.deletestack.pop()
            return -1

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
