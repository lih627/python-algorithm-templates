from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if not words:
            return ''
        all_words = set()
        graph_words = set()
        from collections import defaultdict, deque
        graph = defaultdict(list)
        in_degrees = defaultdict(int)
        for idx, word in enumerate(words):
            all_words = all_words.union(set(list(word)))
            if idx == 0:
                continue
            pre_word = words[idx - 1]
            for i in range(min(len(pre_word), len(word)) + 1):
                # 对于 ['xxxx', 'xx'] 特判
                if i == min(len(pre_word), len(word)):
                    if pre_word[i:] != '':
                        return ''
                    continue
                if pre_word[i] == word[i]:
                    continue
                else:
                    graph[pre_word[i]].append(word[i])
                    in_degrees[word[i]] += 1
                    graph_words.add(pre_word[i])
                    graph_words.add(word[i])
                    break
        res = ''
        # 只有一个字母直接返回
        if len(all_words) == 1:
            for _ in all_words:
                return _

        que = deque()
        for char in all_words:
            if in_degrees[char] == 0:
                que.append(char)

        while que:
            char = que.popleft()
            res += char
            for nex in graph[char]:
                in_degrees[nex] -= 1
                if in_degrees[nex] == 0:
                    que.append(nex)
        if len(res) != len(all_words):
            return ''
        return res
