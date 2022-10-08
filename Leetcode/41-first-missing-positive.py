class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        missingNum = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            if nums[i] == missingNum:
                missingNum += 1
        return missingNum

sol = Solution();
print(sol.firstMissingPositive([2, 1]))