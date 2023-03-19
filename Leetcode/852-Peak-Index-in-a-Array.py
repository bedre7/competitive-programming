class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        start = 1
        end = n - 2
        
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid + 1]:
                start = mid + 1
            elif arr[mid - 1] > arr[mid + 1]:
                end = mid - 1
        
        return -1