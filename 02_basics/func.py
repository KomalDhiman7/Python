def square(number):   


#++++++++++++++orrrr\
    return number **8
result = square(6)
print(result)

def add(num1,num2):
    return num1 +num2
print(add (1,2))

def multiply(p1,p2):
    return p1*p2
print(multiply(8,5))
print(multiply('a',6))
print(multiply(2,'a'))
 
import math
def circle_stats(radius):
    area= math.pi *radius**2
    circumference = 2*math.pi*radius
    return area , circumference
print(circle_stats(3))  

def greet(name = "Komal"):
    return "hello, "+name + " !"
print(greet())

def add(a,b):
    return a +b
result = add (1,2)

cube = lambda x : x**3
print(cube(3))

def sum_all(*args):
    return sum(args)
    for i in args:
        print(i*2)
    return sum(args)
print(sum_all(1,2,3))
    
def print_kwargs(**kwargs):  #krargs
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_kwargs(name="Koml", cousre="Btech", power = "powerful" )

#In Python, the yield keyword is used in a function to make it a generator. A generator is a special type of iterator that allows you to iterate through a sequence of values. When a function contains the yield keyword, it returns a generator object instead of executing the function. Each call to the generator's __next__() method (or using it in a loop) resumes the function's execution from where it left off and continues until it hits another yield statement.

def evn_gen(limit):
    for i in range(2,limit+1,2):
        yield i            
        
for num in evn_gen(10):
    print(num)

