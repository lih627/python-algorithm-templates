# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        node = self.head
        cnt = 0
        import random
        while node:
            if cnt == 0:
                pick = node
                cnt += 1
            else:
                cnt += 1
                if random.randint(1, cnt) == 1:
                    pick = node
            node = node.next
        return pick.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
