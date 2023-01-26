class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        reshaped = [[] for i in range(r)]
        
        row = 0
        perRow = len(mat) * len(mat[0]) // r

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                reshaped[row].append(mat[i][j])
                if len(reshaped[row]) == perRow:
                    row += 1
                    
        return reshaped