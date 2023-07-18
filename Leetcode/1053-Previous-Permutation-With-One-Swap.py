class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                for j in range(len(arr) - 1, -1, -1):
                    if arr[j] < arr[i - 1]:
                        k = j
                        while k >= 1 and arr[k] == arr[k - 1]: k -= 1
                        arr[i - 1], arr[k] = arr[k], arr[i - 1]
                        break
                break
        
        return arr