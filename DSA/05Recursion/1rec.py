def f1(n):
    if n>0:
        f1(n-1)
        print (n, end=' ')
f1(7)

def f2(s):
    if s>0:
        print(s,end=' ')
        f2(s-1)
f2(4)
  

def f4(j):
    if j>0:
        f4(j-1)
        print(2*j-1,end=' ')
f4(10)

def f5(k):
    if k>0:
        f5(k)
        print(2*k,end=' ')
f4(10)



