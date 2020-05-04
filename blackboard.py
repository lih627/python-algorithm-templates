def maxDiff(num: int) -> int:
    if num < 10:
        return 8
    strnum = str(num)
    x = None
    for s in strnum:
        if s != '9':
            x = s
            break
    if x is None:
        str_max = strnum
    else:
        str_max = ''
        for _ in strnum:
            if _ == x:
                str_max += '9'
            else:
                str_max += _

    y = None
    if strnum.startswith('1'):
        for s in strnum:
            if s not in ['0', '1']:
                y = s
                break
        if y is None:
            str_min = strnum
        else:
            str_min = ''
            for s in strnum:
                if s == y:
                    str_min += '0'
                else:
                    str_min += s
    else:
        y = strnum[0]
        str_min = ''
        for s in strnum:
            if s == y:
                str_min += '1'
            else:
                str_min += s

    print(str_max)
    print(str_min)
    return int(str_max) - int(str_min)


print(list(map(maxDiff, [123121857, 1002, 555, 9, 123456, 10000, 9288, 1111])))
