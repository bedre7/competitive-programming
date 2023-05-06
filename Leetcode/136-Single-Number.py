class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = nums[0]
        
        for i in range(1, len(nums)):
            XOR ^= nums[i]
        
        return XOR