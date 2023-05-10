class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        XOR = nums[0]
        for i in range(1, len(nums)):
            XOR ^= nums[i]
        
        firstOne = 1
        for _ in range(32):
            if XOR & firstOne != 0:
                break
            firstOne <<= 1
        
        group = [0, 0]
        for n in nums:
            if n & firstOne != 0:
                group[0] ^= n
            else:
                group[1] ^= n
        
        return group