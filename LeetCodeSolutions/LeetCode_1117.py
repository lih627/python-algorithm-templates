from queue import Queue


class H2O:
    """
    通过阻塞队列
    """

    def __init__(self):
        self.o = Queue(1)
        self.h = Queue(2)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.put(releaseHydrogen)
        self.res()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.o.put(releaseOxygen)
        self.res()

    def res(self):
        if self.o.full() and self.h.full():
            self.o.get()()
            self.h.get()()
            self.h.get()()


from threading import Semaphore


class H2O:
    """
    通过信号量
    """

    def __init__(self):
        self.o = Semaphore(1)
        self.h = Semaphore(2)
        self.n = 0
        self.o.acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h.acquire()
        releaseHydrogen()
        self.n += 1
        if self.n % 2 == 0:
            self.o.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o.acquire()
        releaseOxygen()
        self.h.release()
        self.h.release()
