#to be retried

class Solution:
    def twoSum(self, nums: list[int], target: int, index: int, sol) -> list[int]:
        myMap = {}
        for i in range(len(nums)):
            if(i == index): continue
            if target - nums[i] in myMap:
                match = [myMap.get(target - nums[i]), i]
                sortedMatch = sorted([nums[index], nums[match[0]], nums[match[1]]])
                if sortedMatch not in sol:
                    return sortedMatch
            myMap[nums[i]] =  i

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sol = []
        for i in range(len(nums)):
            currSol = self.twoSum(nums, -nums[i], i, sol)
            if currSol is not None:
                sol.append(currSol)

        return sol
        
sol = Solution()
print(sol.threeSum([0,1,1]))

