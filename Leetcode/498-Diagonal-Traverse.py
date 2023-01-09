from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                index = i + j
                if index % 2 == 0:
                    diagonals[index].insert(0, mat[i][j])
                else:
                    diagonals[index].append(mat[i][j])
                
        return [item for key in sorted(diagonals.keys()) for item in diagonals[key]]