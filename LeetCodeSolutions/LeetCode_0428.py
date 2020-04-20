"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        # 1[1]3[3,2,4]2[5,6]
        if not root:
            return ''
        from collections import deque
        que = deque([root])
        tmp = "[{}]".format(root.val)
        n = str(len(tmp))
        ans = n + tmp
        while que:
            node = que.popleft()
            if not node.children:
                ans += "0[]"
            else:
                tmp = "[{}]".format(",".join([str(_node.val) for _node in node.children]))
                n = str(len(tmp))
                ans += str(n) + tmp
                que.extend(node.children)
        # 切除尾部'0[]'序列
        while ans and ans[-3:] == "0[]":
            ans = ans[:-3]
        print(ans)
        return ans

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data:
            return None

        length = ''
        idx = 0
        while data[idx] != "[":
            length += data[idx]
            idx += 1
        length = int(length)
        next_idx = idx + length
        root_val = int(data[idx + 1: next_idx - 1])
        root = Node(root_val, [])
        idx = next_idx

        from collections import deque
        que = deque([root])
        while idx < len(data):
            # print([_.val for _ in que])
            node = que.popleft()
            if data[idx] == '0':
                idx += 3
                continue
            length = ''
            while data[idx] != '[':
                length += data[idx]
                idx += 1
            length = int(length)
            next_idx = idx + length
            node_vals = [int(_) for _ in data[idx + 1: next_idx - 1].split(',')]
            for val in node_vals:
                _node = Node(val, [])
                node.children.append(_node)
                que.append(_node)
            idx = next_idx
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
