class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        right = middle = float('inf')
        for num in nums:
            if num <= right: right = num
            elif num <= middle: middle = num
            else: return True
        return False