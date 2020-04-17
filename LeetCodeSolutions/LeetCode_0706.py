class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.n = 859
        self.hashmap = [None] * self.n

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.n
        if self.hashmap[idx] is None:
            self.hashmap[idx] = LinkedList(key, value)
        else:
            self.hashmap[idx].put(key, value)
        # print(self.hashmap[idx])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.n
        if self.hashmap[idx] is None:
            return -1
        else:
            return self.hashmap[idx].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.n
        if self.hashmap[idx] is None:
            return
        else:
            self.hashmap[idx].remove(key)
            if self.hashmap[idx].isNone():
                self.hashmap[idx] = None


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nex = None


class LinkedList:
    def __init__(self, key, val):
        self.head = ListNode(key, val)

    def get(self, key):
        node = self.head
        while node:
            if node.key == key:
                return node.val
            node = node.nex
        return -1

    def put(self, key, val):
        dummy = ListNode(None, None)
        dummy.nex = self.head
        pre, cur = dummy, self.head
        while cur:
            if cur.key == key:
                cur.val = val
                self.head = dummy.nex
                return
            pre, cur = pre.nex, cur.nex
        pre.nex = ListNode(key, val)
        self.head = dummy.nex
        return

    def remove(self, key):
        dummy = ListNode(None, None)
        dummy.nex = self.head
        pre, cur = dummy, self.head
        while cur:
            if cur.key == key:
                pre.nex = cur.nex
                break
            pre = pre.nex
            cur = cur.nex
        self.head = dummy.nex

    def isNone(self):
        return self.head is None

    def __repr__(self):
        res = []
        node = self.head
        while node:
            res.append("key:{}, val:{}".format(node.key, node.val))
            node = node.nex
        return ' '.join(res)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
