class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.prev = self.head
        self.next= self.head
        self.size = 0
        
    def __findNodeAt(self, index):
        if index >= self.size or index < 0:  return None
        temp = self.head
        for itr in range(index):
            temp = temp.next

        return temp
        
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        return self.__findNodeAt(index).val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0: return
        if index == 0:
            if self.size == 0:
                self.head = Node(val)
                self.head.next = self.head
                self.head.prev = self.head
            else:
                newGuy = Node(val, None, self.head)
                self.head = newGuy
                if newGuy.next:
                    newGuy.next.prev = newGuy
        else:
            prevGuy = self.__findNodeAt(index - 1)
            newGuy = Node(val, prevGuy, prevGuy.next)
            prevGuy.next = newGuy
            if newGuy.next: newGuy.next.prev = newGuy
                
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0: return
        if index == 0:
            self.head = self.head.next
            if self.head: self.head.prev = None
        else:
            prevGuy = self.__findNodeAt(index - 1)
            toDelete = prevGuy.next
            if toDelete.next: 
                toDelete.next.prev = prevGuy
            if prevGuy:
                prevGuy.next = toDelete.next
                
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)