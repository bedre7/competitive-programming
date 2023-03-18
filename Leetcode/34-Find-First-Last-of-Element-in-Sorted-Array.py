class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = 0
        end = n - 1
        output = [-1, -1]
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                output = [mid, mid]
                end = mid - 1
        
        if output == [-1, -1]: return output
        
        start = output[0]
        end = n - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                output[1] = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        
        return output