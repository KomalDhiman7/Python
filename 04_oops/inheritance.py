class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")

class Toyota(Car):
    def __init__(self, name):
        self.name=name

car1=Toyota("fortuner")
car2=Toyota("prius")
# print(car1.name)
# print(car1.start())

#types of INHERITANCE
# single INH
# multi-level INH
# Multiple INH


##################### Super Method ###################### (inherting parent class)
class Toyoto(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

car1=Toyota("fortuner","electric")
print(car1.type)
