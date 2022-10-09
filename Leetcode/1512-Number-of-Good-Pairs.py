class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n, goodPairs = len(nums), 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] == nums[i]:
                    goodPairs += 1
        
        return goodPairs