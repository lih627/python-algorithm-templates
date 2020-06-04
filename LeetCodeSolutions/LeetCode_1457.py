# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        from collections import deque, defaultdict
        que = deque()

        def isvalid(l):
            counter = collections.Counter(l)
            cnt = 0
            for k in counter:
                if counter[k] & 1:
                    cnt += 1
                if cnt > 1:
                    return False
            return True

        que.append([root, [root.val]])
        res = 0
        while que:
            node, cur_path = que.popleft()
            if not node.left and not node.right:
                if isvalid(cur_path):
                    res += 1
            if node.left:
                que.append([node.left, cur_path + [node.left.val]])
            if node.right:
                que.append([node.right, cur_path + [node.right.val]])
        return res
