class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start = 0
        n = len(citations)
        end = n - 1
        
        while start <= end:
            mid = (start + end) // 2
            if citations[mid] < n - mid:
                start = mid + 1
            else:
                end = mid - 1
        
        return n - start