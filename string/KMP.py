def kmp(pat: str, strs: str) -> int:
    if not pat:
        return 0

    def get_next(pat):
        _next = [0] * len(pat)
        _next[0] = -1
        i, j = 0, -1
        while i < len(pat) - 1:
            if j == -1 or pat[i] == pat[j]:
                i += 1
                j += 1
                _next[i] = j
            else:
                j = _next[j]
        return _next

    _next = get_next(pat)
    i, j = 0, 0
    while i < len(strs) and j < len(pat):
        if j == -1 or strs[i] == pat[j]:
            i += 1
            j += 1
        else:
            j = _next[j]

    if j == len(pat):
        return i - len(pat)
    else:
        return -1


if __name__ == '__main__':
    strs = 'hello'
    pat = 'll'
    print(kmp(pat, strs))
