class RandomizedCollection:
    def __init__(self):
        self.d = collections.defaultdict(set)
        self.v = []

    def insert(self, val: int) -> bool:
        self.d[val].add(len(self.v))
        self.v.append(val)
        return True if len(self.d[val]) == 1 else False

    def remove(self, val: int) -> bool:
        if not self.d[val]:
            return False
        select_idx = self.d[val].pop()
        repalce_val = self.v[-1]
        repalce_idx = len(self.v) - 1
        self.d[repalce_val].add(select_idx)
        self.d[repalce_val].discard(repalce_idx)
        self.v[select_idx] = repalce_val
        self.v.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.v)
