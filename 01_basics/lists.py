# lists are Mutuable

tea = ["Black","Green","oolang"]
tea [1:2]= ["Lemon"]
print(tea)
print(tea[1:1])
tea[1:1]= ["tea_1"]
print (tea)
print (tea[1:3])
tea[1:3] = []
print(tea)

for key in tea :
    print (key)
  print (key , end='-')

if "oolang" in tea:
    print("I have oolang tea")
tea.append("bow")
print (tea)    
tea.pop()
print(tea)




#+++++++++++++++++ list+++++ comprehensionn+++++++++++++++++++++++
square_nums= [x**2 for x in range (10)]
print (square_nums)