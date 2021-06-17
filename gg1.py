class queue():

    def __init__(self,capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.q = [None]*capacity
        self.capacity = capacity

    def isfull(self):
        return self.size == self.capacity

    def isempty(self):
        return self.size == 0

    
    def enqueue(self,item):
        if self.isfull():
            print("full")
            return

        self.rear = (self.rear+1) % (self.capacity)
        self.q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueued to queue"%str(item))

    def dequeue(self):
        if self.isempty():
            print("Empty")
            return 

        print("% s dequeued from queue" % str(self.q[self.front]))
        self.front = (self.front+1) % (self.capacity)
        self.size = self.size - 1

    def quefront(self):
        if self.isempty():
            print("Empty")
        print("front item is", self.q[self.front])

    def querear(self):
        if self.isempty():
            print("Empty")
        print("rear item is",self.q[self.rear])

# driver mode
if __name__ == "__main__":
    q = queue(30)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.dequeue()
    q.quefront()
    q.querear()
    
