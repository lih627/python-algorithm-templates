# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        res, p = head, head
        while k:
            p = p.next
            k -= 1
        while p:
            res = res.next
            p = p.next
        return res
