class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n = len(beginWord)
        from collections import defaultdict, deque
        edges = defaultdict(set)
        for s in [beginWord] + wordList:
            for i in range(n):
                edges[s[:i] + '*' + s[i + 1:]].add(s)

        que = deque()
        que.append((beginWord, 1))
        visited = set([beginWord])
        while que:
            node, cnt = que.popleft()
            keys = []
            for i in range(n):
                keys.append(node[:i] + '*' + node[i + 1:])
            for key in keys:
                for node in edges[key]:
                    if node not in visited:
                        if node == endWord:
                            return cnt + 1
                        visited.add(node)
                        que.append((node, cnt + 1))

        return 0
