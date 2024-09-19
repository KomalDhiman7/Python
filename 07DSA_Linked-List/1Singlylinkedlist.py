#"  define a class node to describe a node in singly linked list"

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next= None

node1 = Node(1)
node2= Node(2)
node3= Node(3)

node1.next= node2
node2.next=node3

#"Define a class SLL to implement singly linked list with __init__ method to create and initiatee start refernce variable "

class SLL:
    def __init__(self, start= None):
        self.start= start

        
#"define a method is _empty() to check if linked list is empty in SLL class"
    def emptyList(self):
        self.start==None
        return True
        
#"in class SLL , define a method insert_at_start() to insert an element at the strating of the list"

    def insert_at_start(self,data):
        if data is None:
            return #
        new_node = Node(data)
        new_node.next = self.start
        self.start= new_node

#define a method to insert at last

    def insert_at_last(self, data):
        new_node=Node(data)
        new_node.next = None
        self.data= new_node
    
#"Define a method to search the node in SLL class"

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None   
      
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp= self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start

            if temp.item ==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                    
            
            
        
        
        
        
        
myList= SLL()
print(myList) 