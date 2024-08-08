import ctypes


class MyList:

    def __init__(self):
        self.size=1
        self.n=0
        self.A=self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n== self.size:
            self.__resize(self.size*2)
        self.A[self.n]=item
        self.n+=1
    
        
    def __str__(self):
        result=''
        for i in range(self.n):
            result+=str[:-1](self.A[i])+","

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity
my_list=MyList()
my_list.append(1)
print(my_list)