class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        left = m - 1
        right = n - 1
        index = m + n -1
        
        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[index] = nums1[left]
                left -= 1
                index -= 1
            else:
                nums1[index] = nums2[right]
                right -= 1
                index -= 1
        
        return nums1