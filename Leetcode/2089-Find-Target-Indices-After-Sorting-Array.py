class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []
        return self.findIndices(nums, target, 0, len(nums) - 1, indices)
    def findIndices(self, nums, target, startIndex, endIndex, indices):
        midIndex = (startIndex + endIndex) // 2
        if startIndex <= endIndex:
            if nums[midIndex] > target:
                self.findIndices(nums, target, startIndex, midIndex - 1, indices)
            elif nums[midIndex] < target:
                self.findIndices(nums, target, midIndex + 1, endIndex, indices)
            elif nums[midIndex] == target:
                indices.append(midIndex)
                self.findIndices(nums, target, midIndex + 1, endIndex, indices)
                self.findIndices(nums, target, startIndex, midIndex - 1, indices)
        
        indices.sort()
        return indices