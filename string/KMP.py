def kmp(pat: str, strs: str) -> int:
    '''
    Get the first pat index if pat in strs
    :param pat:
    :param strs:
    :return:
    '''
    if not pat:
        return 0

    def _get_next(pat):
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

    _next = _get_next(pat)
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


def get_next(pat: str) -> list:
    '''
    _next 数组为 PMT像有偏移1位,并将首位置 -1
    :param pat:
    :return:
    '''
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


def get_pmt(pat: str) -> list:
    '''
    Partial Match Table
    :param pat:
    :return:
    '''
    i, n = 1, len(pat)
    pmt = [0] * n
    while i < n:
        j = pmt[i - 1]
        while j > 0 and pat[i] != pat[j]:
            j = pmt[j - 1]
        if pat[i] == pat[j]:
            j += 1
        pmt[i] = j
        i += 1
    return pmt


def get_nextval(pat):
    '''
    pat[i] == pat[next[i]]
     配位失败不需要返回next[i], 而是next[next[i]]
     如果不相等, 配位失败返回 next[i]
    '''
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
    nextval = _next[:]
    for i in range(2, len(pat)):
        if (pat[i] == pat[_next[i]]):
            nextval[i] = nextval[_next[i]]
    return nextval


if __name__ == '__main__':
    strs = 'hello'
    pat = 'll'
    print(kmp(pat, strs))
    print(get_pmt('aabaaab'))
    print(get_next('ababaabab'))
    print(get_nextval('ababaabab'))
