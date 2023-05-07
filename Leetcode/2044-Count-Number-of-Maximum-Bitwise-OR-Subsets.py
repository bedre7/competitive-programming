from collections import defaultdict

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def findSubsets():
            subsets = [[]]
            
            for i in range(len(nums)):
                for j in range(len(subsets)):
                    if i not in subsets[j]:
                        subsets[j].append(i)
                        subsets.append(subsets[j].copy())
                        subsets[j].pop()
            
            subsets.remove([])
            for i in range(len(subsets)):
                curr = subsets[i]
                subsets[i] = [nums[c] for c in curr]
            return subsets
        
        subsets = findSubsets()
        
        ORs = defaultdict(int)
        maxOR = float('-inf')
        count = 0
        for subset in subsets:
            OR = 0
            for s in subset:
                OR |= s
            
            ORs[OR] += 1
            if OR >= maxOR: 
                maxOR = OR
                count = ORs[OR]
        
        return count