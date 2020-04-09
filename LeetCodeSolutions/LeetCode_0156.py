class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        parent = parent_right = None
        while root:
            root_left = root.left
            root_right = root.right
            root.left = parent_right
            root.right = parent
            parent = root
            parent_right = root_right
            root = root_left
        return parent
