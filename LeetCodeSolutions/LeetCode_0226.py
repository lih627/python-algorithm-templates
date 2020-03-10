class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            helper(node.left)
            helper(node.right)

        helper(root)
        return root
