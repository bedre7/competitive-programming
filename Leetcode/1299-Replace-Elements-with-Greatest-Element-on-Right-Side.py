class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output = [-1] * len(arr)
        
        for i in range(len(arr) - 2, -1, -1):
            output[i] = max(arr[i + 1], output[i + 1])
        
        return output
        