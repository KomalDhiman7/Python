from typing import SupportsIndex


class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()   #as pop is a method in its parent class and in child class so we call super method
        else:
            raise IndexError("Stack is EmPty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    def size(self):
        return len(self)
    

# list class has a insert method

    def insert(self, index,data):
        raise AttributeError
    
s1= Stack()
s1.push(10)
s1.push(89)
s1.push(90)
print(s1.size())