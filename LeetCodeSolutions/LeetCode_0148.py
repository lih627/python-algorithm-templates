# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.sort()
        root = ListNode(res[0])
        tmp = root
        for i in res[1:]:
            tmp.next = ListNode(i)
            tmp = tmp.next
        return root
