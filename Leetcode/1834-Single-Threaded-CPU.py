class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sortedTasks = sorted([[et, pt, i] for i, (et, pt) in enumerate(tasks)])
        order, minHeap = [], []
        i, time, n = 0, sortedTasks[0][0], len(tasks)
        
        while i < n or minHeap:
            while i < n and sortedTasks[i][0] <= time:
                heapq.heappush(minHeap, [sortedTasks[i][1], sortedTasks[i][2]])
                i += 1
            if minHeap:
                processingTime, index = heapq.heappop(minHeap)
                time += processingTime
                order.append(index)
            elif i < n:
                time = sortedTasks[i][0]
        
        return order