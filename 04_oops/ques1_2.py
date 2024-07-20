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

###############2que####################

#abstraction and encapsulation

#create  Account class with 2 attributes- balance & account no.
#create methods for debit, credit and priniting the balance

class Account:
    def __init__(self, bal,acc_no):
        self.bal= bal
        self.acc_no= acc_no

    #debit
    def debit(self, amount):
        self.bal = -amount
        print ( "Money is debited from your account ***** " )

    def credit(self, amount):
        self.bal= amount
        print(" Money is credited in  your account ***** " )
        

    def avl_bal (self):
        return self.bal

    
c1= Account(4500, 767676767)
print(c1.acc_no)

c1.avl_bal()

###################3que############
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius
    
c1=Circle(7)
print(c1.perimeter())
    
