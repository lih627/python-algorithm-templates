# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        stack2 = []
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        ans = None
        while stack1 or stack2 or carry:
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            tmp = a + b + carry
            if tmp > 9:
                carry = 1
                tmp = tmp % 10
            else:
                carry = 0
            cur_node = ListNode(tmp)
            cur_node.next = ans
            ans = cur_node
        return ans
