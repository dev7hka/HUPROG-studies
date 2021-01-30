class Stack:  # LinkedList based stack

    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = Stack.Node()
        self.size = 0

    def push(self, data):
        node = Stack.Node(data)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        return data

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        tmp = self.head.next.data
        self.head.next = self.head.next.next
        return tmp

    def peek(self):
        if self.size == 0:
            return -1
        return self.head.next.data

    def isEmpty(self):
        return self.size == 0

class Solution:

    def removeDuplicates(self, S: str) -> str:

        stack = Stack()
        for _ in S:  # every character in string is traversed
            if stack.peek() == _:  # if top element of stack is same with character, stack's last element is popped
                stack.pop()
            else:
                stack.push(_)  # character is pushed to stack
        result = ""
        while not stack.isEmpty():
            result = stack.pop() + result  # since stack is LIFO, result is reverse added
        return result