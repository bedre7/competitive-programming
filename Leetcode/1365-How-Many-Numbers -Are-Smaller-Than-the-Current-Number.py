class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        valToIndexMap = {}
        
        for i in range(n):
            if nums[i] in valToIndexMap:
                valToIndexMap[nums[i]].append(i)
            else:
                queue = deque()
                queue.append(i)
                valToIndexMap[nums[i]] = queue
        
        nums.sort()
        for i in range(n):
            index = valToIndexMap[nums[i]].popleft()
            smallerVals = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    smallerVals += 1
            output[index] = smallerVals
                
        return output
