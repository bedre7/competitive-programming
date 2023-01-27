from collections import defaultdict, deque
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        valToIndexMap = defaultdict(deque)

        for i in range(n):
            valToIndexMap[nums[i]].append(i)
        
        nums.sort()
        for i in range(n):
            index = valToIndexMap[nums[i]].popleft()
            smallerVals = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    smallerVals += 1
            output[index] = smallerVals
                
        return output