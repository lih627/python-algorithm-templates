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

    def reverseKGroup_(self, head: ListNode, k: int) -> ListNode:
        # Space O(1)
        if k == 1:
            return head
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            cnt = k
            while cnt and tail.next:
                tail = tail.next
                cnt -= 1
            if cnt:
                break
            head = pre.next
            while pre.next != tail:
                cur = pre.next
                pre.next = cur.next
                cur.next = tail.next
                tail.next = cur
            tail = head
            pre = tail
        return dummy.next
