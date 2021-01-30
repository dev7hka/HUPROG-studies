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
        self.top -= 1
        return item

    def peek(self):
        if self.top == 0:
            return None
        return self.lis[self.top - 1]

    def size(self):
        return self.top

    def isEmpty(self):
        return self.top == 0


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
