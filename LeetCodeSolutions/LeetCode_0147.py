# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        cur = head.next
        while cur:
            if pre.val <= cur.val:
                pre.next = cur
                pre = cur
                cur = cur.next
            else:
                insert_pre = dummy
                insert_nxt = dummy.next
                pre.next = None
                while insert_nxt.val < cur.val:
                    insert_pre = insert_pre.next
                    insert_nxt = insert_nxt.next
                insert_pre.next = cur
                _tmp = cur.next
                cur.next = insert_nxt
                cur = _tmp
        return dummy.next
