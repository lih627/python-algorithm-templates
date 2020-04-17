# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node

    def predeccssor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right and not root.left:
                return None
            elif root.right:
                root.val = self.successor(root).val
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predeccssor(root).val
                root.left = self.deleteNode(root.left, root.val)
        return root
