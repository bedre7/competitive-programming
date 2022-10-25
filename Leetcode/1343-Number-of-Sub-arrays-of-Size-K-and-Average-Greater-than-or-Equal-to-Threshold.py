class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = output = total = 0
        
        for r in range(len(arr)):
            total += arr[r]
            if r - l + 1 == k:
                if total // k >= threshold:
                    output += 1
                total -= arr[l]
                l += 1
        
        return output
                