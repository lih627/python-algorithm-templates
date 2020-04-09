# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0
            return 1 + helper(node.left) + helper(node.right)

        return helper(root)

    def countNodes_2(self, root: TreeNode) -> int:
        """
        判断子树是否为完全二叉树
        对于完全二叉树, 直接计算节点个数
        """

        def helper(node):
            if not node:
                return 0
            l_height = r_height = 1
            tmp = node
            while tmp.left:
                tmp = tmp.left
                l_height += 1
            tmp = node
            while tmp.right:
                tmp = tmp.right
                r_height += 1
            if l_height == r_height:
                return 2 ** l_height - 1
            return 1 + helper(node.left) + helper(node.right)

        return helper(root)
