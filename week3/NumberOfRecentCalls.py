class Queue: # linkedList-based Queue

    class Node:
        def __init__(self, data= None):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = self.front
        self.size = 0

    def enqueue(self, data):
        node = Queue.Node(data)
        if self.size == 0:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size +=1
        return data

    def dequeue(self):
        if self.isEmpty():
            return None
        tmp = self.front
        self.front = self.front.next
        self.size -=1
        if self.isEmpty():
            self.rear = None
        return tmp.data

    def peekFront(self):
        if self.front != None:
            return self.front.data
        return None

    def peekRear(self):
        if self.rear != None:
            return self.rear.data
        return None

    def isEmpty(self):
        return self.size == 0

class RecentCounter:

    def __init__(self):
        self.requestList = Queue()

    def ping(self, t: int) -> int:
        self.requestList.enqueue(t)  # new ping is inserted
        while(self.requestList.peekFront() < t-3000): # the pings smaller than "t-3000" are removed
            self.requestList.dequeue()
            if self.requestList.isEmpty():
                break
        return self.requestList.size # remaining queue size is the answer

