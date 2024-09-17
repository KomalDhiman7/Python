class Node:
    def __init__(self,data=None):
        self.data = data
        self.next= None

class Stack:
    def __init__(self, start= None):
        self.start= start

    def emptyList(self):
        self.start==None
        return True

    def insert_at_start(self,data):
        if data is None:
            return #
        n = Node(data,self.start)
        self.start= n

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None   
      
    def pop(self):
        if self.start is None:
            data=self.start.item
            self.start=self.start.next
            return data
        else:
            raise IndexError("Error")
                
myList= Stack()
print(myList) 