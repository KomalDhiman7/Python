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
        
