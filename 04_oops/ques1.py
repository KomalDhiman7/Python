# create student class that takes name& marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    college_name = "CGC"
    name =" anonymous"
    def __init__(self,name,marks):
        self.name = name
        self.marks= marks

    def avg_marks(self):
        sum = 0
        for value in self.marks:
            sum+=value
        print("HY", self.name, "Your score is: ", sum/3)

s1 = Student ("Tony",[80,89,76])
s1.avg_marks()