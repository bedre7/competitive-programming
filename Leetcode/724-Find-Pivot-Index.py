class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        leftSum, rightSum = [0] * size, [0] * size
        
        currSum = 0
        for i in range(size):
            leftSum[i] = currSum
            currSum += nums[i]
        
        currSum = 0
        for i in range(size - 1, -1, -1):
            rightSum[i] = currSum
            currSum += nums[i]
        
        for i in range(size):
            if leftSum[i] == rightSum[i]:
                return i
            
        return -1