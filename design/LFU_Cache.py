class DLinkedListNode:
    def __init__(self, key=None, value=None, frequency=None):
        self.key = key
        self.value = value
        # 记录频率
        self.frequency = frequency
        self.pre = None
        self.nxt = None

    def __repr__(self):
        return "k:{}, v{}, f:{}".format(self.key, self.value, self.frequency)


class LFUCache:
    """
    双向链表 O(N) 查找
    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = DLinkedListNode()
        self.tail = DLinkedListNode()
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def _add_node(self, node):
        # 找到需要node的下一个节点
        nxt_node = self._find_node(node.frequency)
        # 插入 node
        pre_node = nxt_node.pre
        pre_node.nxt = node
        node.pre = pre_node
        node.nxt = nxt_node
        nxt_node.pre = node
        # 将 node 放入字典中
        self.cache[node.key] = node

    def _update_node(self, node):
        """
        更新node
        把node从双向链表取出后插入到正确的位置
        """
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        self._add_node(node)

    def _del_node(self, node):
        """
        删除 node, 维持双向链表不能断裂
        """
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        del self.cache[node.key]

    def _find_node(self, fre):
        """
        返回第一个频率小于等于freq的节点
        """
        _node = self.head.nxt
        while _node.frequency is not None and _node.frequency > fre:
            _node = _node.nxt
        return _node

    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1
        node = self.cache.get(key)
        if not node:
            return -1
        else:
            node.frequency += 1
            self._update_node(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None

        node = self.cache.get(key)
        if node is None:
            # 新建一个 node
            node = DLinkedListNode(key, value, 1)
            # 如果满了, 先删除一个节点
            # 这个节点肯定是 tail 之前的节点
            if len(self.cache) == self.capacity:
                self._del_node(self.tail.pre)
            # 把 node 加入进去
            self._add_node(node)
        else:
            # 如果 node 已经存在, 更新 node 频率和双向链表
            node.frequency += 1
            node.value = value
            self._update_node(node)


class DLinkedListNode:
    def __init__(self, key=None, value=None, frequency=None):
        self.key = key
        self.value = value
        self.freq = frequency
        self.pre = None
        self.nxt = None

    def __repr__(self):
        return "k:{}, v{}, f:{}".format(self.key, self.value, self.freq)


def get_dlinkedlist():
    head = DLinkedListNode()
    tail = DLinkedListNode()
    head.nxt = tail
    tail.pre = head
    return head, tail


class LFUCache:

    def __init__(self, capacity: int):
        import collections
        self.capacity = capacity
        self.size = 0
        self.freq_map = collections.defaultdict(get_dlinkedlist)
        self.key_map = {}
        # min_freq 用于删除节点的时候
        self.min_freq = 0

    def _add_node(self, node):
        """
        在频率字典加入新的节点
        """
        freq = node.freq
        head = self.freq_map[freq][0]
        node.nxt = head.nxt
        node.pre = head
        head.nxt = node
        node.nxt.pre = node

    def _del(self, freq):
        node = self.freq_map[freq][1].pre
        self._remove(node)
        # del the node in key_map
        self.key_map.pop(node.key)

    def _remove(self, node):
        """
        remove node from freq_map[node.freq]
        if freq_map[node.freq] has no useful node,
        del freq_map[node.freq]
        """
        pre_node = node.pre
        nxt_node = node.nxt
        freq = node.freq
        # 如果当前的freq_map[freq] 没有有效节点
        # 删掉当前的key
        # 否则 维持双向链表不断裂
        if self.freq_map[freq] == (pre_node, nxt_node):
            self.freq_map.pop(freq)
        else:
            pre_node.nxt = nxt_node
            nxt_node.pre = pre_node

    def _update_node(self, node, val):
        """
        更新 node
        频率字典受到影响
        """
        self._remove(node)
        # 如果 min_freq 与当前node相同且对应 freq_map 键值被删除
        # min_freq 需要自增1
        if node.freq == self.min_freq and node.freq not in self.freq_map:
            self.min_freq += 1
        # 更新 node 的频率和对应的 value 后, 加入到 freq_map
        node.freq += 1
        node.value = val
        self._add_node(node)

    def get(self, key: int) -> int:
        node = self.key_map.get(key, None)
        if node is None:
            return -1
        else:
            self._update_node(node, node.value)
            return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return None
        if key in self.key_map:
            node = self.key_map[key]
            self._update_node(node, value)
        else:
            node = DLinkedListNode(key, value, 1)
            if self.size == self.capacity:
                self._del(self.min_freq)
                self.size -= 1
            self.min_freq = 1
            self._add_node(node)
            self.key_map[key] = node
            self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
