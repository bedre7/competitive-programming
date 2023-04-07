class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        
        for num in nums:
            for i in range(len(subsets)):
                if num not in subsets[i]:
                    copy = subsets[i].copy()
                    copy.append(num)
                    subsets.append(copy)
                
        return subsets
     
        