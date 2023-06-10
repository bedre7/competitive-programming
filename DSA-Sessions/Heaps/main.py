class Heap:
    def __init__(self, array):
        self.heap = []
        for n in array:
            self.heappush(n)
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, current):
        if current == 0: return
        parent = self.getParentIndex(current)
        if self.heap[parent] > self.heap[current]:
            self.swap(parent, current)
        
        self.heapify_up(parent)
    
    def heapify_down(self, current):
        if current >= len(self.heap): return
        leftChildIndex = self.leftChildIndex(current)
        rightChildIndex = self.rightChildIndex(current)
        
        toSwap = -1
        if rightChildIndex >= len(self.heap):
            if leftChildIndex >= len(self.heap): return
            if self.heap[leftChildIndex] < self.heap[current]:
                toSwap = leftChildIndex
        else:
            toSwap = leftChildIndex if self.heap[leftChildIndex] <= self.heap[rightChildIndex] else rightChildIndex

        if toSwap != -1 and self.heap[current] > self.heap[toSwap]:
            self.swap(toSwap, current)
            self.heapify_down(toSwap)

    def getParentIndex(self, index):
        return (index - 1) // 2

    def leftChildIndex(self, index):
        return 2 * index + 1
    
    def rightChildIndex(self, index):
        return 2 * index + 2
    
    def heappush(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        self.heapify_up(current)
    
    def heappop(self):
        if not self.heap: return None
        element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return element

    def print(self):
        print(self.heap)

# heap = Heap([2, 4, 5, 7, 9, 10])
# heap.heappush(3)
# heap.print()
# print(heap.heappop())
# heap.print()

heap = Heap([1, 2, 3, 4, 5, 6, 7, 8, 9])
# heap.heappush(0)
heap.print()
print(heap.heappop())
heap.print()

