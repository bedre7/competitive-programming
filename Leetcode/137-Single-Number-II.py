class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 1
        missing = 0
        for i in range(32):
            ones = 0
            for n in nums:
                ones += 1 if mask & n != 0 else 0
            
            if ones % 3 != 0:
                missing |= mask
            mask <<= 1
            
        negatives = 0
        for n in nums:
            if n < 0: negatives += 1
        
        if negatives % 3 != 0:
            missing -= 2 ** 32
            
        return missing