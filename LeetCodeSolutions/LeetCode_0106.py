class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def _build(l1, r1, l2, r2):
            if l1 > r1:
                return None
            if l1 == r1 or l2 == r2:
                return TreeNode(postorder[l2])
            root = TreeNode(postorder[r2])
            idx = inorder.index(root.val)
            root.left = _build(l1, idx - 1, l2, l2 + idx - 1 - l1)
            root.right = _build(idx + 1, r1, l2 + idx - l1, r2 - 1)
            return root

        n = len(inorder)
        return _build(0, n - 1, 0, n - 1)
