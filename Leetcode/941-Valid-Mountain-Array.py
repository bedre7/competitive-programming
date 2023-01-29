class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        wasIncreasing = wasDecreasing = False
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                if not wasDecreasing:
                    wasIncreasing = True
                else:
                    return False
            elif arr[i] < arr[i - 1]:
                if not wasIncreasing:
                    return False
                wasDecreasing = True
            else:
                return False
        
        return wasIncreasing and wasDecreasing