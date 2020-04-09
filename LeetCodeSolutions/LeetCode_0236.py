# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        paths = []

        def helper(node, path):
            if not node:
                return
            if node == p or node == q:
                paths.append(path + [node])
                return
            path.append(node)
            helper(node.left, path)
            helper(node.right, path)
            path.pop()

        helper(root, [])
        if len(paths) == 1:
            return paths[-1][-1]
        p1, p2 = paths[0], paths[1]
        n1, n2 = len(p1), len(p2)
        for i in range(min(n1, n2) - 1, -1, -1):
            if p1[i] == p2[i]:
                return p1[i]
