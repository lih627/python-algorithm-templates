class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        visited = collections.defaultdict(int)
        v = set()
        ret = []
        for name in names:
            if name not in visited:
                ret.append(name)
                visited[name] += 1
            else:
                n = visited[name]
                cnt = 0
                while name + '(' + str(n + cnt) + ')' in visited:
                    cnt += 1;
                visited[name] += cnt;
                name += '(' + str(n + cnt) + ')'
                ret.append(name)
                visited[name] += 1
        return ret
