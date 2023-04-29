class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        maxPos = float('-inf')
        for _, f, t in trips: maxPos = max(maxPos, f, t)

        prefix = [0] * (maxPos + 2)

        for i in range(len(trips)):
            passengers, _from, to = trips[i]
            prefix[_from] += passengers
            prefix[to] += -passengers
        
        for i in range(1, maxPos):
            prefix[i] += prefix[i - 1]
        prefix.pop()

        for currentPassengers in prefix:
            if currentPassengers > capacity:
                return False

        return True