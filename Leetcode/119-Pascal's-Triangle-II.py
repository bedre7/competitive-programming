class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if 0 <= rowIndex <= 1:
            return [1] * (rowIndex + 1)
        
        prev = self.getRow(rowIndex - 1)
        new = []
        for i in range(rowIndex - 1):
            new.append(prev[i] + prev[i + 1])
        
        return [1] + new + [1]