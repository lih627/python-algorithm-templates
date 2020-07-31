from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.l1 = Lock()
        self.l2 = Lock()
        self.l2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.l1.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.l2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.l2.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.l1.release()
