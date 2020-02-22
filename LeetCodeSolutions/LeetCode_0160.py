# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB
        la = lb = 0
        while pA:
            pA = pA.next
            la += 1
        while pB:
            pB = pB.next
            lb += 1
        if la < lb:
            la, lb = lb, la
            headA, headB = headB, headA
        cnt = la - lb
        while cnt:
            headA = headA.next
            cnt -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
