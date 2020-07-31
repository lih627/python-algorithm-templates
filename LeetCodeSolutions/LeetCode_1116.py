from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self._zero = Lock()
        self._odd = Lock()
        self._even = Lock()
        self._odd.acquire()
        self._even.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self._zero.acquire()
            printNumber(0)
            if i & 1:
                self._odd.release()
            else:
                self._even.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self._even.acquire()
            printNumber(i)
            self._zero.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self._odd.acquire()
            printNumber(i)
            self._zero.release()
