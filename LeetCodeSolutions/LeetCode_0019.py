# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = head
        right = head
        while n > -1:
            if not right:
                return head.next
            right = right.next
            n -= 1

        while right:
            left, right = left.next, right.next
        left.next = left.next.next
        return head
