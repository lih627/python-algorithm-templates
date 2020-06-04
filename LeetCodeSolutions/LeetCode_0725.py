# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = 0
        node = root
        while node:
            n += 1
            node = node.next
        base_len = n // k;
        additional_node = n - base_len * k;
        res = []
        node = root
        for i in range(k):
            res.append(node)
            addi = 0
            if additional_node > 0:
                additional_node -= 1
                addi = 1
            if node:
                for _ in range(base_len + addi - 1):
                    if node:
                        node = node.next
            nxt = None
            if node:
                nxt = node.next
                node.next = None
            node = nxt
        return res
