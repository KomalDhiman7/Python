import ctypes

class MyList:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def append(self, Item):
        if self.n == self.size:
            self.__resize(self.size * 2)
        self.A[self.n] = Item
        self.n += 1

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.size = new_capacity

    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __str__(self):
        result = ''
        for i in range(self.n):
            result += str(self.A[i]) + ', '
        return '[' + result[:-2] + ']'

# Example usage:
my_list = MyList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list)  # Output should be: [1, 2, 3]
print(len(my_list))  # Output should be: 3
