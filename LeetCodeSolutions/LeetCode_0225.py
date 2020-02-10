class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.q1 = deque()
        self.q2 = deque()

    #         from queue import Queue
    #         self._que1 = Queue()
    #         self._que2 = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while self.q2:
            self.q1.append(self.q2.popleft())
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())

        # while not self._que2.empty():
        #     self._que1.put(self._que2.get())
        # self._que2.put(x)
        # while not self._que1.empty():
        #     self._que2.put(self._que1.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return
        # return self._que2.get()
        return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return
        # tmp = self._que2.get()
        return self.q2[0]
        # return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        # return self._que1.empty() and self._que2.empty()
        return not self.q2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
