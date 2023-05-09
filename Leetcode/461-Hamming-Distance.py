class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        XOR = x ^ y
        mask = 1
        ones = 0
        
        for i in range(32):
            ones += 1 if XOR & mask != 0 else 0
            mask <<= 1
            
        return ones