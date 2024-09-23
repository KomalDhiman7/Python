class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.item_count==0
    
    def insert_front(self,data):
        N=Node(data,None,self.front)
        if self.is_empty():
            self.front=N
            self.rear=N
        else:
            self.front=N
            self.front.prev=N
        self.item_count+=1

    def insert_rear(self,data):
        N=Node(data,self.rear)
        if self.is_empty():
            self.front=N
        else:
            self.rear.next=N
        self.rear=N
        self.item_count+=1

    def delete_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
        self.item_count-=1
    
    def get_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.item
    
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.item

    def size(self):
        return self.item_count        
        
deque=Deque()
deque.insert_front(90)
deque.insert_rear(80)
deque.insert_front(80)
print(deque.is_empty())
print("Size of deque is", deque.size())