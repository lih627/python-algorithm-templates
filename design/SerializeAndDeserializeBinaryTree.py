# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """
    Serialize and Deserialize A Binary Tree
     1
    / \
       2
      / \
         3
        / \
        4  5
    serialize: '1 # 2 # 3 4 5 # # # #'

    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        from collections import deque
        que, res = deque(), []
        que.append(root)
        while que:
            node = que.popleft()
            if not node:
                res.append('#')
            else:
                res.append(str(node.val))
                que.extend([node.left, node.right])
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split()
        if not nodes:
            return None
        from collections import deque
        nodes = deque(nodes)
        root = TreeNode(int(nodes.popleft()))
        que = deque()
        que.append(root)
        while nodes:
            node = que.popleft()
            if not node:
                continue
            l = nodes.popleft()
            l = int(l) if l != '#' else None
            if l is not None:
                node.left = TreeNode(l)
                que.append(node.left)
            r = nodes.popleft()
            r = int(r) if r != '#' else None
            if r is not None:
                node.right = TreeNode(r)
                que.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    from data_structures.binarytree import buildTreeFromList
    from data_structures.binarytree import printTree

    nums = [1, 2, 3, None, 4, None, 5, None, None, None, 6, None, None, 7, 8]
    root = buildTreeFromList(nums)
    printTree(root)
    codec = Codec()
    print(codec.serialize(root))
    nums3 = [1,
             None, 2,
             None, None, None, 3,
             None, None, None, None, None, None, 4, 5
             ]
    root2 = buildTreeFromList(nums3)
    printTree(root2)
    print(codec.serialize(root2))
