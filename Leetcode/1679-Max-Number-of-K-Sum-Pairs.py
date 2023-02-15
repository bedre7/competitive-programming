from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        numDict = Counter(nums)
        
        for num in nums:
            if k - num in numDict:
                if k - num == num:
                    if numDict[num] >= 2:
                        numDict[num] -= 2
                        operations += 1
                elif numDict[k - num] != 0 and numDict[num] != 0:
                    numDict[k - num] -= 1
                    numDict[num] -= 1
                    operations += 1
        
        return operations