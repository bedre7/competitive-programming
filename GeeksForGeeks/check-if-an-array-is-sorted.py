#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        left = 0
        right = 1
        
        while right < n:
            if arr[left] > arr[right]:
                return False
            left += 1
            right += 1
        
        return True