class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def backtrack(start, partition):
            if start == n:
                return len(partition) > 1
            
            for i in range(start, n):
                if not partition or partition[-1] - int(s[start: i + 1]) == 1:
                    partition.append(int(s[start: i + 1]))
                    if backtrack(i + 1, partition):
                        return True
                    partition.pop()
            
            return False
        
        return backtrack(0, [])
        
