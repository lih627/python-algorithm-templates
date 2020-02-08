# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(node):
            if not node:
                return None
            if not node.next:
                return node
            tmp = node.next
            node.next = helper(node.next.next)
            tmp.next = node
            return tmp

        return helper(head)
