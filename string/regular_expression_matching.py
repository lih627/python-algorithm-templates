'''
Given an input string s and a pattern p.
implement regular expression matching with support
for '.' and '*'

'.' matches any single character
'*' matches zero or more of the preceding element
'''


def isMatch_1(s, p):
    if not p:
        return not s
    pre = s and p[0] in ['.', s[0]]
    if len(p) > 1 and p[1] == '*':
        return isMatch_1(s, p[2:]) or pre and isMatch_1(s[1:], p)
    else:
        return pre and isMatch_1(s[1:], p[1:])


def isMatch_dp(s, p):
    if not p: return not s
    if not s and len(p) == 1: return False
    '''
    dp[i][j] = dp[i-1][j-1] if s[i] == p[j] or p[j] == '.'
             = dp[i][j-2]   if p[j] == '*' ,p[j-1]!=s[i]
             = dp[i][j-2] or dp[i-1][j] if p[j] == '*', p[j-1] =='.' or p[j-1] == s[i]
             = False else
    '''
    m, n = len(s) + 1, len(p) + 1
    dp = [[False for _ in range(n)] for _ in range(m)]
    dp[0][0] = True
    # initial
    for j in range(2, n):
        y = j - 1
        if p[y] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m):
        for j in range(1, n):
            x, y = i - 1, j - 1
            if p[y] in {s[x], '.'}:
                dp[i][j] = dp[i - 1][j - 1]
            if p[y] == '*':
                if p[y - 1] not in {s[x], '.'}:
                    dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
    return dp[-1][-1]


if __name__ == '__main__':
    s = ['aa', 'aa', 'ab', 'aab', 'mississippi']
    p = ['a', 'a*', '.*', 'c*a*b', 'mis*is*p*']
    for func in (isMatch_1, isMatch_dp):
        for ss, pp in zip(s, p):
            print(func.__name__, func(ss, pp))
