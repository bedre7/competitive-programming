class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirs = [
                [1, 1], [-1, 1], [1, -1], [-1, -1], 
                [1, 0], [0, 1], [-1, 0], [0, -1]
               ]
        
        def isInBound(row, col):
            return row in range(0, 9) and col in range(0, 9)
        
        canAttack = []
        for L, R in dirs:
            left = king[0] + L
            right = king[1] + R
            while isInBound(left, right):
                if [left, right] in queens:
                    canAttack.append([left, right])
                    break
                else:
                    left += L
                    right += R
            
        return canAttack