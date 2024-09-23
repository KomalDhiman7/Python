class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def insert_at_first(self, data):
        n = Node(data)
        if self.is_empty():
            self.start = n
            n.next = self.start
        else:
            current = self.start
            while current.next != self.start:
                current = current.next
            current.next = n
            n.next = self.start
            self.start = n

    def print_list(self):
        temp = self.start
        if temp is None:
            print("List is empty")
            return
        while True:
            print(temp.item, end=" ")
            temp = temp.next
            if temp == self.start:
                print("START")
                break


cll = CLL()
cll.start = Node(1)
cll.start.next = Node(2)
cll.start.next.next = Node(3)
cll.start.next.next.next = cll.start

cll.print_list()