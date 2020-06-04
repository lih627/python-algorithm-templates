class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        fs = [set(_) for _ in favoriteCompanies]
        n = len(favoriteCompanies)
        flag = [True] * n
        for idx, s in enumerate(fs):
            for j in range(n):
                if idx != j and flag[idx] and flag[j] and s.issubset(fs[j]):
                    flag[idx] = False
                    break
        return [idx for idx, val in enumerate(flag) if val]
