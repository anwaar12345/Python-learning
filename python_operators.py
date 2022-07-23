from pprint import pprint


print("the sum of 3 + 2 = ", 3 + 2)
print("the sum of 3 - 2 = ", 3 - 2)
print("the sum of 3 / 3 = ", 3 / 3) # division will always return float  1.0
print("the sum of 3 * 2 = ", 3 * 2) 

age = 27
age +=  1 #equal to age = age + 2
age -= 1
age *= age 
age /= 27
age = 1
print("older") if age > 0 and age == 27 else print("younger") #ternary

print(age > 30)
print("age: ",age)
print(age > 2 or age ==0)
print(type(1/1))