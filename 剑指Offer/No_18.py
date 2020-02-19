# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        cur = head
        while cur.val != val:
            cur = cur.next
            pre = pre.next
        pre.next = pre.next.next
        return dummy.next
