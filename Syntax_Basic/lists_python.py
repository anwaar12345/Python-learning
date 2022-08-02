import os
clear = lambda: os.system('clear')
clear()
''' we can create list items of diffrent types '''
# persons = [("anwar","27"),("Computer Scientist","Programmer")]
fruits = [ "Apple", "Banana", "Orange", 1, 2.2, True]
fruits[-1] = "Mango"
print(fruits[1:len(fruits)])