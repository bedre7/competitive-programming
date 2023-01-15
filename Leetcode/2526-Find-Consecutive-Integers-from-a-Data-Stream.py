from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.dataStream = deque()

    def consec(self, num: int) -> bool:
        if self.dataStream and self.dataStream[-1] != num:
            while self.dataStream:
                self.dataStream.pop()
        
        if len(self.dataStream) >= self.k:
            self.dataStream.popleft()
        
        self.dataStream.append(num)
        
        return len(self.dataStream) == self.k and self.dataStream[-1] == self.value


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)