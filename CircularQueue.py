class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = k
        self.deque = []
        self.front = -1
        self.rear = 0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.deque.insert(0, value)
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.rear += 1
            self.deque.append(value)
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.deque.pop(0)
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.deque.pop()
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.deque:
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.deque:
            return self.deque[-1]
        return -1      

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return (len(self.deque) == 0)
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (len(self.deque) == self.size)



obj = MyCircularDeque(6)
obj.insertFront(8)
obj.insertLast(9)
obj.deleteFront()
obj.deleteLast()
obj.getFront()
obj.getRear()
obj.isEmpty()
obj.isFull()
# obj.display()

