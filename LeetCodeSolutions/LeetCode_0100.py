# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSameTree(self, p, q):
        '''
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
        '''
        que = [(p, q)]

        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val == q.val:
                return True
            return False

        while que:
            p, q = que.pop(0)
            if not check(p, q):
                return False
            if p:
                que.extend([(p.left, q.left), (p.right, q.right)])
        return True
