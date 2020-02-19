# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        def reverse(node):
            if not node:
                return None
            if not node.next:
                return node
            last = reverse(node.next)
            node.next.next = node
            node.next = None
            return last

        return reverse(head)
