class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        size = len(matrix)
        transpose = []

        for i in range(size):
            for j in range(len(matrix[i])):
                if len(transpose) <= j: transpose.append([])
                transpose[j].append(matrix[i][j])

        return transpose