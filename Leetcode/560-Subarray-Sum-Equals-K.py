class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        preSum = {0: 1}
        subArrays = 0
        
        for n in nums:
            currSum += n
            diff = currSum - k
            if diff in preSum:
                subArrays += preSum[diff]
            preSum[currSum] = 1 + preSum.get(currSum, 0)
        
        return subArrays