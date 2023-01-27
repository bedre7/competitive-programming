class Solution: 
    def select(self, arr, i):
        minIndex = i
        for j in range(i, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        return minIndex
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minIndex = self.select(arr, i)
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
        
        return arr