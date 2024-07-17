usernam="komal"
def func():
    usernam="sam"
    print(usernam)
print(usernam)
func()

#######################

x=99
def func2(y):
    z=x+y
    return z
result=func2(3)  #y=3
print(result)

########################

def func3():
    x=6
    print(x)
print(x)
func3()

#######################

def f1():
    x=88
    def f2():
        print(x)
    return f2
myResult =f1()     #closure or bag theory
myResult()

########################

def ko(num):
    def mal(x):
        return x ** num    #factory functions
    return mal
