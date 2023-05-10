class Solution:
    def countArrangement(self, n: int) -> int:
        beautifulOnes = 0
        
        def permute(result):
            nonlocal beautifulOnes
            if len(result) == n:
                beautifulOnes += 1
                return
            
            for i in range(1, n + 1):
                if i not in result:
                    index = len(result) + 1
                    if i % index == 0 or index % i == 0:
                        result.append(i)
                        permute(result)
                        result.pop()
                    
        for i in range(1, n + 1):
            if i % 1 == 0 or 1 % i == 0:
                permute([i])
        
        return beautifulOnes