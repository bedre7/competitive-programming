class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def makeSn(n):
            if n == 1: return "0"
            
            prev = makeSn(n - 1)
            inverted = ''.join(['0' if c == '1' else '1' for c in prev])
            
            return prev + "1" + inverted[::-1]
        
        return makeSn(n)[k - 1]