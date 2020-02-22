# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodea, nodeb = headA, headB
        while nodea != nodeb:
            nodea = nodea.next if nodea else headB
            nodeb = nodeb.next if nodeb else headA
        return nodea
