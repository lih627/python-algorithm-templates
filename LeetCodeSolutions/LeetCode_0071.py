class Solution:
    def simplifyPath(self, path: str) -> str:
        elems = path.split('/')
        res = []
        for tmp in elems:
            if tmp == '..':
                if res:
                    res.pop()
            elif tmp and tmp != '.':
                res.append(tmp)
        return '/' + '/'.join(res)
