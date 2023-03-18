class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x // 2 + 1
        ans = None
        while start <= end:
            mid = (start + end) // 2
            squared = mid ** 2
            if squared > x:
                end = mid - 1
            elif squared < x:
                ans = mid
                start = mid + 1
            else:
                return mid
        
        return ans