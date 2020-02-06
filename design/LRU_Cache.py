from collections import OrderedDict


class LRU_Cache_v1(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            # FIFO
            self.popitem(last=False)


class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRU_Cache_v2():
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        '''
        Always add the new node right after head
        '''
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        '''
        Remove an existing node from the linked list
        '''
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        '''
        Move certain node in vetween to the head
        '''
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        '''
        Pop the current tail
        '''
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        node = self.cache.get(key)

        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                # Del node
                del self.cache[tail.key]
                self.size -= 1

        else:
            node.value = value
            self._move_to_head(node)


if __name__ == '__main__':
    for _ in (LRU_Cache_v1, LRU_Cache_v2):
        cache = LRU_Cache_v2(2)
        res = [
            cache.put(1, 1),
            cache.put(2, 2),
            cache.get(1),
            cache.put(3, 3),
            cache.get(2),
            cache.put(4, 4),
            cache.get(1),
            cache.get(3),
            cache.get(4)
        ]
        print(res)
