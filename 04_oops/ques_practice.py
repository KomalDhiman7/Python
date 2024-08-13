# # class Car:
# #     def __init__(self,brand,model):
# #         self.brand = brand
# #         self.model= model

# # c1= Car("toyoto","2022")
# # print(c1.model)

# class Circle:
#     def __init__(self, radius):
#         self.radius= radius        

#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14*self.radius
    
# c1= Circle(2)
# print(c1.area())

class Person:
    def __init__(self, name, country, dob):
        self.name= name
        self.country= country
        self.dob= dob

    def age(self):
        return 2024-self.dob
    
p1= Person("Komal","India",2003)

print(p1.age())
    
