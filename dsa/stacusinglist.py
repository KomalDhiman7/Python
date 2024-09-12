class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Cannot pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)
    
stack = Stack()
print(stack.is_empty())  

stack.push(19)
stack.push(56)
stack.push(88)

print(stack.items) 

print(stack.pop()) 
print(stack.size())  