# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        slow = fast = head
        if not head.next:
            return TreeNode(head.val)
        while slow.next and fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next
            if not fast:
                break
            else:
                fast = fast.next
        root = TreeNode(slow.val)
        root.right = self.sortedListToBST(slow.next)
        pre.next = None
        root.left = self.sortedListToBST(head)
        return root
