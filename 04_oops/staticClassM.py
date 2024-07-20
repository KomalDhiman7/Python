#Methods that dont use self parameter(work at class level)
# @staticmethod (decorator)
 
#methods are functions belong to objects.

class Student:
    college_name="CGC"
    name ="anonymous"    

    def __init__(self, name, marks):    
        self.name= name        
        self.marks=marks
        print("adding value to database")

    @staticmethod               #decorator (static method)
    def hello():
        print("hello")

    def welcome(self):
        print("Welcome to CGC", self.name)

# s1=Student("komal",87)     
# s1.welcome()

##  Class Method  = bounds

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1= Student()
p1.changeName("Rahul")
print(Student.name)



#stitc methods= doesn't  access class or instance methods
#class methods= cls attribute
#instance attribute = self sttribute

        
