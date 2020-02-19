class Solution:
    def isNumber(self, s: str) -> bool:
        state = 'START'
        s = s.lstrip().rstrip()
        for i in s:
            state = self.trans(state, i)
            if state == 'END':
                return False
        return state in ['INTEGER', 'FLOAT', 'SCIENCE']

    def trans(self, state, x):
        sign = ['+', '-']
        numbers = [str(i) for i in range(10)]
        ex = ['e', 'E']
        point = ['.']
        if state == 'START':
            if x in sign:
                return 'SIGN1'
            if x in point:
                return 'POINT'
            if x in numbers:
                return 'INTEGER'
        if state == 'SIGN1':
            if x in point:
                return 'POINT'
            if x in numbers:
                return 'INTEGER'
        if state == 'POINT':
            if x in numbers:
                return 'FLOAT'
        if state == 'INTEGER':
            if x in numbers:
                return state
            if x in point:
                return 'FLOAT'
            if x in ex:
                return 'EXPONENT'
        if state == 'FLOAT':
            if x in numbers:
                return state
            if x in ex:
                return 'EXPONENT'
        if state == 'EXPONENT':
            if x in sign:
                return 'SIGN2'
            if x in numbers:
                return 'SCIENCE'
        if state == 'SIGN2':
            if x in numbers:
                return 'SCIENCE'
        if state == 'SCIENCE':
            if x in numbers:
                return 'SCIENCE'
        return 'END'
