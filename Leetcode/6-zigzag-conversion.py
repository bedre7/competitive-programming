class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [''] * numRows
        
        inc = 1
        zigzagIndex = 0
        for i in range(len(s)):
            zigzag[zigzagIndex] += s[i]
            if zigzagIndex == numRows - 1:  inc = -1
            elif zigzagIndex == 0: inc = 1
            if numRows > 1 : zigzagIndex += inc
        
        return ''.join(zigzag)