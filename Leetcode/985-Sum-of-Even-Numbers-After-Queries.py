class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumArray = []
        
        even_sum = 0
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        for val, index in queries:
            old_val = nums[index]
            if old_val % 2 == 0:
                even_sum -= old_val
            
            nums[index] += val
            
            if nums[index] % 2 == 0:
                even_sum += nums[index]
                
            sumArray.append(even_sum)
        
        return sumArray