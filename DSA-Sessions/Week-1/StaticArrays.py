class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        self.arr = arr
        self.capacity = capacity
        self.length = length
   
    def insertEnd(self, value):
        if self.length < self.capacity:
            self.arr[self.length] = value
            self.length += 1

    def removeEnd(self):
        if self.length > 0:
            self.arr[self.length] = 0
            self.length -= 1
   
    def insertMiddle(self, index, value):
        if self.length >= self.capacity:
            return

        for i in range(self.length - 1, index + 1, -1):
            self.arr[i + 1] = self.arr[i]
        
        self.arr[index] = value
        self.length += 1
       
    def removeMiddle(self, index):
        if index >= self.length or index < 0:
            return
        
        for i in range(index, self.length - 1):
            self.arr[i + 1] = self.arr[i]
        
        self.length -= 1
   
    def printArr(self):
        for i in range(self.length):
            print(self.arr[i], end=" ")
