class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed and not popped:
            return True
        aux = []
        idx = 0
        for _ in pushed:
            aux.append(_)
            while aux and aux[-1] == popped[idx]:
                aux.pop()
                idx += 1
        return not aux
