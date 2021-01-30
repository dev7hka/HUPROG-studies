class Queue: # array-based queue implementation

    def __init__(self):
        self.lis = []
        self.size = 0

    def enqueue(self, item):
        self.lis.append(item)
        self.size +=1

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.lis.pop(0)
        self.size -=1
        return item

    def front(self):
        if self.size ==0:
            return None
        return self.lis[self.size-1]

    def rear(self):
        if self.size == 0:
            return None
        return self.lis[0]

    def isEmpty(self):
        return self.size == 0

class RecentCounter:

    def __init__(self):
        self.requestList = Queue()

    def ping(self, t: int) -> int:  # new ping is inserted
        self.requestList.enqueue(t)
        while(self.requestList.rear() < t-3000): # the pings smaller than "t-3000" are removed
            self.requestList.dequeue()
        return self.requestList.size


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)