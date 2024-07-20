#methods are functions belong to objects.

class Student:
    college_name="CGC"
    name ="anonymous"    

    def __init__(self, name, marks):    
        self.name= name        
        self.marks=marks
        print("adding value to database")

    def welcome(self):
        print("Welcome to CGC", self.name)

s1=Student("komal",87)     
s1.welcome()

############ Decorators ##############\

class Clas:
    def Marks(self,phy,chem,maths):
        self.phy = phy
        self.chem= chem
        self.maths= maths

    # def Percent(self):
    #     self.percent=((self.phy+self.chem+self.maths)/3)+"%"

    @property
    def percent(self):
        return str((self.phy+self.chem+self.maths)/3)+"%"
stu1 = Clas(98,98,99)
stu1.phy = 95
print(stu1.percent)


        
