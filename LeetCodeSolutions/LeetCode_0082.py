# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        while pre and pre.next:
            cur = pre.next
            nxt = cur.next
            while nxt and cur.val == nxt.val:
                tmp = cur.val
                cur = nxt
                while cur.val == tmp and cur.next:
                    cur = cur.next
                if not cur.next:
                    if cur.val == tmp:
                        cur = None
                    break
                nxt = cur.next
            pre.next = cur
            pre = pre.next
        return dummy.next
