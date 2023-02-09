class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxArea = float('-inf')
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            if height[left] <= height[right]:
                maxArea = max(maxArea, height[left] * width)
                left += 1
            else:
                maxArea = max(maxArea, height[right] * width)
                right -= 1
        
        return maxArea