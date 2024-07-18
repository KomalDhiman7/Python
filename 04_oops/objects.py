#creating class

class Student:
    def  __init__(self):
        print("adding new student in database")
    name="komal"
    
# creating object

s1 = Student()
print(s1.name)

# __init__ Function (constructor= invokes while creating an an object)

# the "Self" parameter is a reference to the current instance of the class ,and is used to access the variabls that belongs to the class

class Student:
    college_name="CGC"
    name ="anonymous"    #class atttribute

    def __init__(self, name, marks):    
        self.name= name          #object attribute>>class attr(priority)
        self.marks=marks
        print("adding value to database")

s1=Student("komal",87)     #object
print(s1.name)
        
