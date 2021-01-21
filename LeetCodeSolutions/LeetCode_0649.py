from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qs = deque()
        qd = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                qs.append(i);
            else:
                qd.append(i);
        n = len(senate)
        while qs and qd:
            s, d = qs.popleft(), qd.popleft()
            if s < d:
                qs.append(s + n);
            else:
                qd.append(d + n);
        if qs: return 'Radiant'
        return 'Dire'
