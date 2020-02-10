class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._in = []
        self._out = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        return self._out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        if not self._out:
            return self._in[0]
        return self._out[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self._in == [] and self._out == []

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
