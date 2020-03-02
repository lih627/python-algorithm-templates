# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists_(self, lists: List[ListNode]) -> ListNode:
        '''
        prehead = ListNode(-1)
        pre = prehead
        tmp = []
        for _ in lists:
            while _:
                tmp.append(_.val)
                _ = _.next
        tmp.sort()
        while tmp:
            pre.next = ListNode(tmp.pop(0))
            pre = pre.next
        return prehead.next
        '''
        import heapq
        dummy = ListNode(-1)
        pre = dummy
        head = []
        cnt = 0
        for _ in range(len(lists)):
            while lists[_]:
                heapq.heappush(head, (lists[_].val, cnt, lists[_]))
                cnt += 1
                lists[_] = lists[_].next
        while head:
            idx, cur_cnt, pre.next = heapq.heappop(head)
            pre = pre.next
        return dummy.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        '''
        heapqlist
        '''
        ListNode.__lt__ = lambda x, y: x.val < y.val
        heap = [_ for _ in lists if _]
        dummy = ListNode(None)
        node = dummy
        heapq.heapify(heap)
        while heap:
            node.next = heapq.heappop(heap)
            node = node.next
            if node.next:
                heapq.heappush(heap, node.next)
        return dummy.next
