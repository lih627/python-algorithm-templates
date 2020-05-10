class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row, col = binaryMatrix.dimensions()
        i, j = 0, col - 1
        while -1 < i < row and -1 < j < col:
            if binaryMatrix.get(i, j) == 1:
                j -= 1
            else:
                i += 1
        if j == col - 1:
            return -1
        else:
            return j + 1
