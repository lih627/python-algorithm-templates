# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isSame(t1, t2):
    if not t1 or not t2:
        if not t1 and not t2:
            return True
        return False
    return isSame(t1.left, t2.left) and isSame(t1.right, t2.right)


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True

        def helper(node1, node2):
            stack = [[node1, False]]
            while stack:
                node, visited = stack.pop()
                if not visited:
                    if node.val == node2.val:
                        if isSame(node, node2):
                            return True
                    if node.left:
                        stack.append([node.left, False])
                    stack.append([node, True])
                    if node.right:
                        stack.append([node.right, False])
            return False

        return helper(t1, t2)
