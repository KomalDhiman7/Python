age = 6
input ("what's your age:  ")
if age < 18:
    print("teen")
elif age <50:
    print("Adult")
else:
    print("Old")
    
# 2. question

age = 19
if age <8 :
    print("Price = 100")
elif age >9:
    print("price = 200")

# 3. question

score = 84
if score >90:
    print("A")
elif score >80:
    print ("B")
else :
    print("Fail")

# 4. question

fruit = "apple"
color = "red"
if fruit =="apple":
    if color =="yellow":
        print("Kacha hai bhai")
else:
    print("pkk gya , mai kahne jariii")

# 5. question


weather = "clear"
if weather == "rainy":
    print("sleep")
else :
    print ("walk")


#. 8. question

password = "Asfwjsghkwen$"
password_len = len(password)

if password_len <6:
    print("change the password")
else:
    print("Strong")

# 7.question

order = "Medium"
extra = True
if extra:
    coffee = order + " coffee and extra"
else:
    coffee = order +"coffee"
print("order: " , coffee)

