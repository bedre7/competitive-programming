class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        
        def backtrack(result, start):
            if len(result) == k:
                output.append(result.copy())
            
            for i in range(start, n + 1):
                if i not in result:
                    result.append(i)
                    backtrack(result, i + 1)
                    result.pop()
        
        for i in range(1, n + 1):
            backtrack([i], i)
        
        return output