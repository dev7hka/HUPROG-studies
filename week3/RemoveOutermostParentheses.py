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

    def removeOuterParentheses(self, S: str) -> str:
        result = []      # ultimate result
        res = ""         # individual results
        self.stack = Stack()
        for _ in S:
            res += _
            if _ == ")" and self.stack.peek() == "(": # if closing an open parantheses, remove from stack
                self.stack.pop()
            else:
                self.stack.push(_)
            if self.stack.isEmpty():      # if stack empty, a primitive is generated.
                result.append(res[1:-1])  # remove outermost parantheses and add to the result
                res = ""
        return "".join(result)
