class Queue(list):
    def is_empty(self):
        return len(self)==0

    def enqueue(self, item):
            self.append(item)
    

    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            print("Error")

    def size(self):
        return len(self) 
    
    def get_front(self):
        return self[0]

    def get_rear(self):
        return self[-1]

q=Queue()
q.enqueue(10)
q.enqueue(12)
q.enqueue(89)
q.dequeue()
print(q.size())
print(q.is_empty())
