class MyQueue:

    def __init__(self):
        self.stack = []
        self.customQ = []
        
    def push(self, x: int) -> None:
        if self.customQ:
            while self.customQ:
                self.stack.append(self.customQ.pop())
        
        self.stack.append(x)                
                
    def pop(self) -> int:
        if self.stack:
            while self.stack:
                self.customQ.append(self.stack.pop())
        
        return self.customQ.pop()

    def peek(self) -> int:
        if self.stack:
            while self.stack:
                self.customQ.append(self.stack.pop())
        
        return self.customQ[-1]
    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.customQ) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()