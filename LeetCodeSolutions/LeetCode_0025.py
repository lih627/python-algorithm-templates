# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # from powcai
        # Space O(k), k in [1, n]
        if k == 1:
            return head
        dummy = ListNode(None)
        p = dummy
        while True:
            cnt = k
            stack = []
            tmp = head
            while cnt and tmp:
                stack.append(tmp)
                tmp = tmp.next
                cnt -= 1
            if cnt:
                p.next = head
                break
            head = tmp
            while stack:
                p.next = stack.pop()
                p = p.next
        return dummy.next
