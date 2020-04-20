# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        import collections
        visited = collections.Counter()
        res = []

        def dfs(node):
            if not node:
                return '#'
            serial = "{},{},{}".format(node.val, dfs(node.left), dfs(node.right))
            visited[serial] += 1
            if visited[serial] == 2:
                res.append(node)
            return serial

        dfs(root)

        return res
