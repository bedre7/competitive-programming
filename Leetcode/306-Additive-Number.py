class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n <= 2: return False
        
        def backtrack(start, seq):
            if start == n:
                return len(seq) >= 3
            
            for i in range(start, n):
                curr = num[start: i + 1]
                if (not (len(curr) > 1 and curr.startswith('0')) and 
                    (len(seq) <= 1 or seq[-1] + seq[-2] == int(curr))):
                    seq.append(int(curr))
                    if backtrack(i + 1, seq):
                        return True
                    seq.pop()
                    
            return False
        
        return backtrack(0, [])