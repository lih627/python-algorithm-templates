# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p.next:
            cur = p.next
            nxt = cur.next
            while nxt and cur.val == nxt.val:
                cur = cur.next
                nxt = cur.next
            p.next = cur
            p = cur
        return dummy.next
