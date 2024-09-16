class StackExtendingList(list):
    # Push element onto the stack
    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self) == 0

    def size(self):
        return len(self)


stack = StackExtendingList()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())  
print(stack.pop())
print(stack.size())  


    