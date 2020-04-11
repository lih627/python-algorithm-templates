class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nums = []
        alphas = []
        for strs in logs:
            if '0' <= strs[-1] <= '9':
                nums.append(strs)
            else:
                alphas.append(strs)
        alphas.sort(key=lambda x: x.split(None, 1)[::-1])
        return alphas + nums
