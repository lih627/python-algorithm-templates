# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        change list to a ring and cut the ring.
        '''
        if not head or k == 0:
            return head
        n = 1
        p = head
        while p.next:
            n += 1
            p = p.next
        if k % n == 0:
            return head
        p.next = head
        k = n - k % n
        while k:
            k -= 1
            pre = head
            head = head.next
        pre.next = None
        return head
