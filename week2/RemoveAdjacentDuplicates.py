class Stack: # array-based stack

    def __init__(self):
        self.lis = []
        self.top = 0

    def push(self, item):
        self.lis.append(item)
        self.top += 1

    def pop(self):
        if self.top == 0:
            return None
        item = self.lis.pop()
        self.top -=1
        return item

    def peek(self):
        if self.top == 0:
            return None
        return self.lis[self.top-1]

    def isEmpty(self):
        return self.top == 0

class Solution:

    def removeDuplicates(self, S: str) -> str:
        self.stack = Stack()
        for _ in S:  # every character in string is traversed
            if self.stack.peek() == _:  # if top element of stack is same with character, stack's last element is popped
                self.stack.pop()
            else:
                self.stack.push(_)   # character is pushed to stack
        result = ""
        while not self.stack.isEmpty():
            result = self.stack.pop() + result  # since stack is LIFO, result is reverse added
        return result