# sum of n natural no.
def sum(n):
    if n==0:
        return 0
    else:
        return n+ sum (n-1)
print(sum(5))

#sum of odd natural no.
def sumodd(m):
    if m == 1:
        return 1
    else:
        return 2*m-1 + sumodd(m-1)
print(sumodd(5))  

# sum of even natural no.
def sumEven(k):
    if k==0:
        return 0
    else:
        return 2*k+sumEven(k-1)
print(sumEven(5))

# calculate factorail of a no.
def fac(j):
    if j==1:
        return 1
    else:
        return j*fac(j-1)
print(fac(3))

def sumSq(h):
    if h==0:
        return 0
    else:
        return h**2 + sumSq(h-1)
print(sumSq(3))



