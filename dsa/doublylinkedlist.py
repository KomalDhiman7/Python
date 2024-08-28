class Node:
    def __init__(self, prev= None, item= None, next = None):
        self.prev= prev
        self.item= item
        self.next= next

class DLL:
    def start_node(self,start= None):
        self.start= start

    def is_empty(self):
        return self.start==None
    
    def insert_at_first(self):
        n = Node(None)
        if not self.is_empty():
            self.start.prev = n
        self.start= n
    
    def insert_at_last(self, data):
        temp =n
        if self.start is not None:
            while temp.next is None:
                temp.next = None
            n=Node(temp,data,None)
            if temp.next==None:
                self.start=n
            else:
                temp.next=n

    def insert_at_last(self, data):
        new_node = Node(None, data, None)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp


    def search(self,data):
        temp= self.start
        while temp is not None:
            if temp.item==data:
                return temp

    def print_all(self,data):
        temp= self.start
        while temp is not None:
            print (temp)

    def delete_first(self):
        temp = self.start
        if self.prev is None:
            self.start==self.start.next

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

    def delete_part_item(self,data):
        temp= self.start
        
            
