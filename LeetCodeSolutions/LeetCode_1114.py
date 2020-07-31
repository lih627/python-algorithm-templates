from threading import Lock


class Foo:
    def __init__(self):
        self.first_job_done = Lock()
        self.second_job_done = Lock()
        self.first_job_done.acquire()
        self.second_job_done.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_job_done.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.first_job_done:
            printSecond()
        self.second_job_done.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.second_job_done:
            printThird()
