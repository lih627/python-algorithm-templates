# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        卡特兰数
        Catalan: https://oi-wiki.org/math/catalan/
        """
        if not n:
            return []

        def helper(start, end):
            if start > end:
                return [None, ]
            all_tree = []
            for i in range(start, end + 1):
                left = helper(start, i - 1)
                right = helper(i + 1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_tree.append(root)
            return all_tree

        return helper(1, n)
