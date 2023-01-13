class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numDict = {}
        
        for i in range(len(nums)):
            numDict[nums[i]] = i
            
        for old, new in operations:
            nums[numDict[old]] = new
            numDict[new] = numDict[old]
        
        return nums