class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        
        for i in range(1, n):
            arr[i] ^= arr[i - 1]
        
        return [arr[r] ^ arr[l - 1] if l != 0 else arr[r] for l, r in queries]