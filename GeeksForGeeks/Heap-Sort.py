#User function Template for python3
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        leftChildIndex, rightChildIndex = 2 * i + 1, 2 * i + 2
        toSwap = i
        
        if leftChildIndex < n and arr[toSwap] < arr[leftChildIndex]:
            toSwap = leftChildIndex
        if rightChildIndex < n and arr[toSwap] < arr[rightChildIndex]:
            toSwap = rightChildIndex
        if toSwap != i:
            arr[toSwap], arr[i] = arr[i], arr[toSwap]
            self.heapify(arr, n, toSwap)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)