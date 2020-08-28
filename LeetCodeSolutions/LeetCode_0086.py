#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1, dummy2 = ListNode(None), ListNode(None)
        p1, p2 = dummy1, dummy2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            nxt = head.next
            head.next = None
            head = nxt
        p1.next = dummy2.next
        return dummy1.next
# @lc code=end
