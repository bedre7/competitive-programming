class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        placeHolder = 0
        seeker = 0
        
        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[seeker], nums[placeHolder] = nums[placeHolder], nums[seeker]
                placeHolder += 1 

            seeker += 1