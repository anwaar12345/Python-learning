#text data types 
import os

clear = lambda : os.system('clear')

clear()

name  = "Syed Anwar Ahmed Shah"

about  = """ 
I am passionate software engineer i have working with stack for last 2.5 years and
 
have worked with Best PHP and most rated framework of the world \"Laravel\" 

also i have worked with lumen, CI and OOP and Procedural PHP i also had an 

opportunity to work with Jquery Ajax 

and Vanilla JavaScript. 

                  Now i am willing to learn new emerging technologies for this i am working on improving 
                      
                  and learning python.

                  After Learning Python and making some projects in it after this i will learn Django, Flask and FastApi 

                  along with that i will learn DB and practice SQL and then will move towards NODEJS and to front end after that i will 

                  learn aws ccp then aws cd .....
"""

print(about)


print(len(about))


print(about.replace('.','!'))


print(about.startswith(' '))

print(about.index('l'))

about.capitalize()

name = "shah"

print(name.upper())

print(name.lower())