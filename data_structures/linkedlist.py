# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_recurrence(node):
    '''
    reverse linked list
    recurrence version
    1->2->3->4->None
    4->3->2->1->None
    '''
    if not node:
        return None
    if not node.next:
        return node
    last = reverse_recurrence(node.next)
    node.next.next = node
    node.next = None
    return last


def reverse(head):
    '''
    reverse linked list
    '''
    pre, cur = None, head
    while cur:
        tmp_next = cur.next
        cur.next = pre
        pre = cur
        cur = tmp_next
    return pre


def print_ll(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next

    print(res + [None])


def build_ll(nums):
    if not nums:
        return None
    dummy = ListNode(None)
    p = dummy
    for _ in nums:
        p.next = ListNode(_)
        p = p.next
    return dummy.next


if __name__ == '__main__':
    import copy

    nums = [1, 2, 3, 4, 5]
    head = build_ll(nums)
    print_ll(head)
    head2 = reverse_recurrence(copy.deepcopy(head))
    print_ll(head2)
    print_ll(head)
