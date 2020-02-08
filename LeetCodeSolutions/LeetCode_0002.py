# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = l1.val + l2.val
        carry = 0 if tmp < 10 else 1
        head = ListNode(tmp % 10)
        res = head
        l1, l2 = l1.next, l2.next
        while l1 and l2:
            tmp = l1.val + l2.val + carry
            carry = 0 if tmp < 10 else 1
            head.next = ListNode(tmp % 10)
            head = head.next
            l1, l2 = l1.next, l2.next
        rest = None
        if l1:
            rest = l1
        if l2:
            rest = l2
        self.addRestList(head, rest, carry)
        return res

    def addRestList(self, res, node, carry):
        while node:
            tmp = node.val + carry
            carry = 0 if tmp < 10 else 1
            res.next = ListNode(tmp % 10)
            res = res.next
            node = node.next
        if carry:
            res.next = ListNode(carry)
