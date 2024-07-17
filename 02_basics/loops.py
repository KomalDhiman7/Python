numbers= [1,2,3,-6,-9,8]
positive_num=0
for num in numbers:
    if num>0:
        positive_num+=1
print("Final count of no. is: ",positive_num)

#sum of even no.

n = 10
sum_even=0
for i in range(1,n+1):
    if i%2==0:
        sum_even+=1
print("sum of even  no. is: ", sum_even)

#print mult table for a given no. up to 10,but skip the 5th iteration

number= 3
for i in range(1,11):
    if i==5:
        continue
    print(number,'x',i,'=', number*i)
    
#reverse a string

input_str="python"
reversed_str=""
for char in input_str:
    reversed_str=char+reversed_str
print(reversed_str)

#find non-repested character

str="independence"
for char in str:
    if str.count(char)==1 :
        print("char is ", char)
        break
    
#factorial
number  =  5
factorial=1
while number>0:
    factorial=factorial*number
    number -=1

print("factorial is ", factorial)


#validate input
while True:
    number = int(input("Enter value b/w 1 &10: "))
    if 1<= number <=10:
        print("thanks")
        break
    else:
        print("invalid")        
        
#prime number checker

number = 29
is_prime=True
if number>1:
    for i in range(2,number):
        if number%i==0:
            is_prime=False
            break
print(is_prime)

#Exponential backoff
import time
wait_time=1
max_retries=5
attempts=0

while attempts<max_retries:
    print("Attempt", attempts+1,"-wait time", wait_time, )
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1

    