# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        from collections import deque
        q = deque()
        while head:
            q.appendleft(head.val)
            head = head.next
        return list(q)
