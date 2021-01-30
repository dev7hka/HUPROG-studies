class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = LinkedList.Node()
        self.length = 0

    def insert(self, data):
        if self.length == 0:
            self.head.data = data
            self.length += 1
            return
        item = LinkedList.Node(data)
        item.next = self.head
        self.head = item
        self.length += 1

    def delete(self, data):
        if self.length == 0:
            return None
        if self.head.data == data:
            ret = self.head
            self.head = self.head.next
            self.length -= 1
            return ret.data
        tmp = self.head
        while tmp.next != None:
            if tmp.next.data == data:
                ret = tmp.next
                tmp.next = tmp.next.next
                self.length -= 1
                return ret.data
            tmp = tmp.next
        return None

    def search(self, data) -> int:
        cur = self.head
        ind = 0
        while cur is not None:
            if cur.data == data:
                return ind
            ind += 1
            cur = cur.next
        return -1

    def setHead(self, head):
        self.head = head
        cur = self.head
        self.length = 0
        while cur is not None:
            self.length +=1
            cur = cur.next

    def isEmpty(self):
        return self.length == 0

    def getHead(self):
        return self.head

    def print(self):
        cur = self.head
        while cur != None:
            print(f"{cur.data}", end="")
            if cur.next != None:
                print(" -> ", end="")
            else:
                print("")
            cur = cur.next

class Guitar:

    def __init__(self):
        self.list = dict()  # the head of each string of guitar is stored

    def add(self, s, f):
        if s in self.list:
            currentList = self.list[s]
            currentNode = currentList.getHead()
            count = 1
            while currentNode is not None and currentNode.data > f:  # right place is found to add fret
                count += 1
                currentNode = currentNode.next
            if currentNode is not None:
                if currentNode.data == f:
                    self.list[s].setHead(currentNode)
                    return count-1
            head = LinkedList()
            head.insert(f)
            head.getHead().next = currentNode
            self.list[s] = head
            return count
        else: # first time a string inserted
            head = LinkedList()
            head.insert(f)
            self.list[s] = head
            return 1

guitar = Guitar()
N, P = map(int, input().split())
total = 0
for _ in range(N):
    string, fret = map(int, input().split())
    total += guitar.add(string, fret)
print(total)