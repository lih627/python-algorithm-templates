"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
        while p:
            tmp = Node(p.val)
            tmp.next = p.next
            p.next = tmp
            p = tmp.next
        phead = head.next
        p = head
        while p:
            p.next.random = p.random.next if p.random else None
            p = p.next.next
        p = head
        while p:
            tmp = p.next
            p.next = tmp.next
            tmp.next = p.next.next if p.next else None
            p = p.next
        return phead
