class MinStack:
    def __init__(self):
        self.stack1 = []    #to keep all elements
        self.stack2 = []    #to keep track of min elements

    def isEmpty(self):
        return not self.stack1
    
    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.stack2 or val <= self.getMin():
            self.stack2.append(val)

    def pop(self) -> None:
        if self.stack1[-1] == self.getMin():
            self.stack2.pop()
        self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]
    
    def getMin(self) -> int:
        return self.stack2[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()