class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        que = deque([('0000', 0)])

        def _add(x, y):
            return str((int(x) + y) % 10)

        while que:
            cur_strs, step = que.popleft()
            deadends.add(cur_strs)
            step += 1
            for idx, _ in enumerate(cur_strs):
                for j in (-1, 1):
                    tmp = cur_strs[:idx] + _add(_, j) + cur_strs[idx + 1:]
                    if tmp == target:
                        return step
                    if not tmp in deadends:
                        que.append((tmp, step))
                        deadends.add(tmp)
            # print(step, que)
        return -1
        '''
        res = set()
        strs = [str(_) for _ in range(10)]
        _add = strs[1:] + strs[:1]
        _subtract = strs[-1:] + strs[:-1]
        def transstr(x):  
            tmp = []
            if x not in deadends:
                for idx, _ in enumerate(x):
                    addres = x[:idx] + _add[int(_)] + x[idx+1:]
                    subtractres = x[:idx] + _subtract[int(_)] + x[idx+1:]
                    if not addres in res:
                        tmp.append(addres)
                    if not subtractres in res:
                        tmp.append(subtractres)
            return tmp
        if target == '0000':
            return 0
        queue = ['0000']
        cnt = 1
        while queue:
            tmp = []
            for _ in queue:
                res.add(_)
                c = transstr(_)
                res.update(c)
                if target in c:
                    return cnt
                tmp += c
            cnt += 1
            queue = tmp
        return -1
        '''
