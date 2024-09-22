# operaations like making a new node, upadte ,deleet first, last , checking list is empty

class Node:
    def __init__(self,data, prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class CDLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=Node(data)
        if not self.is_empty():
            n.item=data
            n.next=self.start
            n.prev=self.prev

    def print_list(self,data):
        temp=self.start

        while True:
            print(temp.data,end=" ")
            temp= temp.next
            if temp.next==self.start:
                break
        print()

cdll= CDLL()
cdll.insert_at_start(4)
cdll.insert_at_start(5)
cdll.insert_at_start(6)

cdll.print_list()




