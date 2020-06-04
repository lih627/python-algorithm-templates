class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        s = text.split(' ')
        ss = []
        for idx, val in enumerate(s):
            ss.append([val, idx])
        ss.sort(key=lambda x: [len(x[0]), x[1]])
        ret = ' '.join([_[0] for _ in ss])
        return ret[0].upper() + ret[1:]
