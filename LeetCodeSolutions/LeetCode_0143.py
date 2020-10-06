# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse(cur):
    pre = None
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
        slow.next = None
        l2 = reverse(l2)
        l1 = head
        while l1 and l2:
            _nl1 = l1.next
            _nl2 = l2.next
            l1.next = l2
            l2.next = _nl1
            l1 = _nl1
            l2 = _nl2
        return head
