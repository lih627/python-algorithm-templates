from threading import Lock


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.que = []
        self.producer = Lock()
        self.customer = Lock()
        self.customer.acquire()
        self.mutex = Lock()
        self.n = capacity

    def enqueue(self, element: int) -> None:
        self.producer.acquire()
        self.que.append(element)
        if self.size() != self.n:
            self.producer.release()
        if self.customer.locked():
            self.customer.release()

    def dequeue(self) -> int:
        self.customer.acquire()
        ret = self.que.pop(0)
        if self.size():
            self.customer.release()
        if self.producer.locked():
            self.producer.release()
        return ret

    def _size(self):
        return len(self.que)

    def size(self) -> int:
        ret = None
        with self.mutex:
            ret = self._size()
        return ret
