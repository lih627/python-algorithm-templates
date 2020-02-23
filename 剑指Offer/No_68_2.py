# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        paths = []

        def getpath(path, node):
            if path[-1] == node:
                paths.append(path[:])
                return
            if path[-1].left:
                getpath(path + [path[-1].left], node)
            if path[-1].right:
                getpath(path + [path[-1].right], node)

        getpath([root], p)
        getpath([root], q)
        p1, p2 = paths[0], paths[1]
        m, n = len(p1), len(p2)
        for i in range(min(m, n)):
            if p1[i] != p2[i]:
                i -= 1
                break
        return p1[i]

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(node, p, q):
            if not node or node == q or node == p:
                return node
            leftnode = helper(node.left, p, q)
            rightnode = helper(node.right, p, q)
            if not leftnode:
                return rightnode
            if not rightnode:
                return leftnode
            return node

        node = helper(root, p, q)
        return node
