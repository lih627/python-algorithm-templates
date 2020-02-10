# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        # print(head)
        slow, fast = head, head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        def helper(node):
            if not node.next: return node
            last = helper(node.next)
            node.next.next = node
            node.next = None
            return last

        tmp = head
        p1, last = head, helper(slow)
        p2 = last
        while p1 and p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                pre.next = helper(last)
                return False
        pre.next = helper(last)
        # print(head)
        return True
