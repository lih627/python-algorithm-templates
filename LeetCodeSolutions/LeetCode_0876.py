# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        p = pp = dummy
        while pp:
            p = p.next
            if pp.next:
                pp = pp.next.next
            else:
                pp = pp.next
        return p
