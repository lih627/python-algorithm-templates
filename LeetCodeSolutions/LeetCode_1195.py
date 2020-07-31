from threading import Lock


class FizzBuzz:
    def __init__(self, n: int):
        self._n = n
        self.cnt = 1
        self.n = Lock()
        self.f = Lock()
        self.b = Lock()
        self.fb = Lock()
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self._n + 1):
            if i % 3 == 0 and i % 5:
                self.f.acquire()
                printFizz()
                self.cnt += 1
                self._determine()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self._n + 1):
            if i % 3 and i % 5 == 0:
                self.b.acquire()
                self.cnt += 1
                printBuzz()
                self._determine()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self._n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.fb.acquire()
                printFizzBuzz()
                self.cnt += 1
                self._determine()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self._n + 1):
            if i % 3 and i % 5:
                self.n.acquire()
                printNumber(self.cnt)
                self.cnt += 1
                self._determine()

    def _determine(self):
        if self.cnt % 3 and self.cnt % 5:
            if self.n.locked():
                self.n.release()
        elif self.cnt % 3 == 0 and self.cnt % 5:
            if self.f.locked():
                self.f.release()
        elif self.cnt % 3 and self.cnt % 5 == 0:
            if self.b.locked():
                self.b.release()
        else:
            if self.fb.locked():
                self.fb.release()
