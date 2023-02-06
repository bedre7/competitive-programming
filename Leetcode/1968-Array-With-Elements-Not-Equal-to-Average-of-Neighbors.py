from math import ceil
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            swapped = False
            for j in range(1, len(nums) - 1):
                if ceil((nums[j - 1] + nums[j + 1]) / 2) == nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
                    
            if not swapped:
                break
        
        return nums