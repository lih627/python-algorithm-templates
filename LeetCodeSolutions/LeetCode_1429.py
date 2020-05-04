class ListNode:
    def __init__(self, val):
        self.val = val
        self.nex = None
        self.pre = None


class DLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.nex = self.tail
        self.tail.pre = self.head

    def add(self, val):
        # add to the tail
        node = ListNode(val)
        prev = self.tail.pre
        prev.nex = node
        node.pre = prev
        node.nex = self.tail
        self.tail.pre = node
        return node

    def remove(sefl, node):
        prev = node.pre
        next_ = node.nex
        prev.nex = next_
        next_.pre = prev

    def isEmpty(self):
        return self.tail.pre == self.head

    def getFirst(self):
        return self.head.nex.val


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.unique = {}
        self.duplicate = set()
        self.Ullist = DLinkedList()
        for num in nums:
            if num in self.duplicate:
                continue
            if num not in self.unique:
                node = self.Ullist.add(num)
                self.unique[num] = node
            else:
                node = self.unique[num]
                self.Ullist.remove(node)
                self.duplicate.add(num)
                self.unique.pop(num)

    def showFirstUnique(self) -> int:
        if self.Ullist.isEmpty():
            return -1
        else:
            return self.Ullist.getFirst()

    def add(self, value: int) -> None:
        if value in self.duplicate:
            return
        else:
            if value not in self.unique:
                node = self.Ullist.add(value)
                self.unique[value] = node
            else:
                node = self.unique[value]
                self.Ullist.remove(node)
                self.duplicate.add(value)
                self.unique.pop(value)
