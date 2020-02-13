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
    the List is BFS of the TreeNode
    """
    root = TreeNode(elems.pop(0))
    from collections import deque
    que = deque()
    que.append(root)
    while que and elems:
        node = que.popleft()
        left = elems.pop(0)
        right = elems.pop(0)
        if node:
            node.left = TreeNode(left) if left is not None else None
            node.right = TreeNode(right) if right is not None else None
            que.append(node.left)
            que.append(node.right)
        else:
            que.append(None)
            que.append(None)
    return root


def bfsTreeNode(root: TreeNode) -> list:
    """
    BFs TreeNode
    :param root:
    :return:
    """
    if not root:
        return []
    from collections import deque
    que = deque()
    que.append(root)
    res = []
    while any(que):
        node = que.popleft()
        if node:
            res.append(node.val)
            que.append(node.left)
            que.append(node.right)
        else:
            res.append(None)
            que.append(None)
            que.append(None)
    return res


def printTree(root):
    print(bfsTreeNode(root))


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


if __name__ == '__main__':
    root = buildTreeFromList([1, 3, 2, None, None, 7, None])
    print('root1', bfsTreeNode(root))
    pres = PreOrderTraversal(root)
    ins = InOrderTraversal(root)
    print('pres', pres)
    print('inos', ins)
    root2 = buildTreeFromPreInTraversal(pres, ins)
    print('root2', bfsTreeNode(root2))
    printTree(root2)
