# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        cnt = 0
        node = head
        while node:
            cnt += 1
            node = node.next
        stack = []
        res = [0] * cnt
        idx = 0
        node = head
        while node:
            while stack and stack[-1][0] < node.val:
                _, iidx = stack.pop()
                res[iidx] = node.val
            stack.append([node.val, idx])
            idx += 1
            node = node.next
        return res
