from typing import List

null = None
"""
1. build tree from preorder traversal and inorder traversal
2. build tree from list, like leetcode test input
3. print tree from bfs result, like leetcode test output
4. traversals
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTreeFromPreInTraversal(preorder: List[int],
                                inorder: List[int]) -> TreeNode:
    """
    Build binary Tree from inorder traversal and preorder traversal
    LeetCode 105
    """

    def helper(pres, ins):
        if not pres or not ins:
            return None
        root = TreeNode(pres[0])
        idx = ins.index(root.val)
        root.left = helper(pres[1: idx + 1], ins[:idx])
        root.right = helper(pres[idx + 1:], ins[idx + 1:])
        return root

    return helper(preorder, inorder)


def buildTreeFromList(elems: List[int]) -> TreeNode:
    """
    Build Tree From a  List
    the List is Hierarchical traversal of the TreeNode
      1
     / \
    #   2
       / \
      #  3
         /\
        4 #
    elems: [1 # 2 # 3 4]
    """
    from collections import deque
    elems = deque(elems)
    if not elems:
        return None
    root = TreeNode(elems.popleft())
    que = deque()
    que.append(root)
    while que and elems:
        node = que.popleft()
        left = elems.popleft()
        if left is not None:
            node.left = TreeNode(left)
            que.append(node.left)
        if elems:
            right = elems.popleft()
            if right is not None:
                node.right = TreeNode(right)
                que.append(node.right)
    return root


def bfsTreeNode(root: TreeNode) -> list:
    """
    BFs TreeNode
    Hierarchical traversal
    """
    if not root:
        return []
    from collections import deque
    que = deque()
    que.append(root)
    res = [root.val]
    while que:
        node = que.popleft()
        if node.left:
            res.append(node.left.val)
            que.append(node.left)
        else:
            res.append(None)
        if node.right:
            res.append(node.right.val)
            que.append(node.right)
        else:
            res.append(None)
    return res


def printTree(root):
    print(bfsTreeNode(root))


class Traversal():
    '''
    Traversal method for binary tree
    Pre/In/Post Order Traversal methods:
    包含递归和迭代的写法
    包含层次遍历的代码
    '''

    @staticmethod
    def PreOrderStack(root: TreeNode) -> list:
        if not root:
            return []
        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    @staticmethod
    def InOrderStack(root):
        if not root:
            return []
        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    @staticmethod
    def PostOrderStack(root):
        '''
        left right root
        '''
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        while stack1:
            # 招数后序遍历的逆序. 存放在 stack2 中
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node.val)
        return stack2[::-1]

    @staticmethod
    def PreOrderTraversal(root: TreeNode) -> list:
        if not root:
            return []
        res = []

        def helper(node):
            if not node:
                return
            res.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return res

    @staticmethod
    def InOrderTraversal(root: TreeNode) -> list:
        if not root:
            return []
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)

        helper(root)
        return res

    @staticmethod
    def PostOrderTraversal(root: TreeNode) -> list:
        if not root:
            return []
        res = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)

        helper(root)
        return res

    @staticmethod
    def HierarchicalTraversal(root: TreeNode) -> list:
        if not root:
            return []
        from collections import deque
        que = deque()
        que.append(root)
        res = [root.val]
        while que:
            node = que.popleft()
            if node.left:
                res.append(node.left.val)
                que.append(node.left)
            else:
                res.append(None)
            if node.right:
                res.append(node.right.val)
                que.append(node.right)
            else:
                res.append(None)
        return res


if __name__ == '__main__':
    root = buildTreeFromList([1, None, 2, None, 3, None, 4, 5, 6])
    print('root1', bfsTreeNode(root))
    pres = Traversal.PreOrderTraversal(root)
    ins = Traversal.InOrderTraversal(root)
    print('pres', pres)
    print('inos', ins)
    root2 = buildTreeFromPreInTraversal(pres, ins)
    print('root2', bfsTreeNode(root2))
    printTree(root2)
    print(Traversal.InOrderTraversal(root2))
    print(Traversal.InOrderStack(root2))
    print(Traversal.PreOrderTraversal(root2))
    print(Traversal.PreOrderStack(root2))
    print(Traversal.PostOrderTraversal(root2))
    print(Traversal.PostOrderStack(root2))
