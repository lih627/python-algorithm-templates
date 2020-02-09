from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # silding window
        from collections import Counter
        if not s or not words:
            return []
        counter = Counter(words)
        _word = len(words[0])
        len_words = len(words) * _word
        len_s = len(s)
        res = []
        print(counter)
        for i in range(_word):
            left = i
            right = i + len_words
            tmp = []
            for _ in range(left, right, _word):
                tmp.append(s[_: _ + _word])
            cur_counter = Counter(tmp)
            while right <= len_s:
                if cur_counter == counter:
                    res.append(left)
                if cur_counter[s[left: left + _word]] > 1:
                    cur_counter[s[left: left + _word]] -= 1
                else:
                    del cur_counter[s[left: left + _word]]
                left += _word
                right = left + len_words
                cur_counter[s[right - _word: right]] += 1
        return res
