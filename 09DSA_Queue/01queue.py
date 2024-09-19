class Queue(list):

    def is_empty(self):
        return len(self)==0

    def enqueue(self,item):
        self.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            raise IndexError("empty")

    def get_front(self):
        return self[0]

    def get_rear(self):
        return[-1]
        
    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            print("ERROR")

q1= Queue()
q1.enqueue(10)
q1.enqueue(19)
print(q1.size())
        
