from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda x: list(map(order.index, x)))
