class ListNode:
    def __init__(self, val=None, pre=None, nex=None):
        self.val = val
        self.pre = pre
        self.nex = nex

    def __repr__(self):
        return str(self.val) if self.val != None else '#'


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nex = self.tail
        self.tail.pre = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < self.size:
            node = self.head.nex
            for i in range(index):
                node = node.nex
            return node.val
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp = self.head.nex
        node = ListNode(val)
        node.nex = tmp
        tmp.pre = node
        self.head.nex = node
        node.pre = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tmp = self.tail.pre
        node = ListNode(val)
        node.nex = self.tail
        node.pre = tmp
        tmp.nex = node
        self.tail.pre = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif 0 < index < self.size:
            self.size += 1
            node = ListNode(val)
            pre = self.head
            for i in range(index):
                pre = pre.nex
            nex = pre.nex
            node.pre = pre
            pre.nex = node
            node.nex = nex
            nex.pre = node
        return

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if -1 < index < self.size:
            node = self.head.nex
            for i in range(index):
                node = node.nex
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            del node
            self.size -= 1
        return

    def _print(self):
        node = self.head
        while node:
            print(node, end=' ')
            node = node.nex

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
