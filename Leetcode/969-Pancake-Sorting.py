class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        sortedArr = [i + 1 for i in range(len(arr))]
        
        flips = []
        
        while sortedArr:
            currmax = sortedArr.pop()
            index = arr.index(currmax)
            if index != 0:
                arr = arr[:index + 1][::-1] + arr[index + 1:]
                flips.append(index + 1)
                
            remaining = len(sortedArr)
            flips.append(remaining + 1)
            arr = arr[:remaining+1][::-1] + arr[remaining + 1:]
        
        return flips