from datetime import date

'''
variable name is case sensitive 
a varaible name can only start with alphabet or underscore
it also applies to other identifier i.e: class,function
'''
name  = "Syed Anwar Ahmed Shah is learning new skill\"'s"
Name = "new"

print(name)
print(Name)

name_with_out_escapes = '''python is "awesome"  and 'easy to learn' language '''

intro = "%s and %s "%(name,name_with_out_escapes)

new_intro = f"{name} and {name_with_out_escapes}"

print(f'''{intro} {new_intro}''')

age  = date.today().year - date(1995,3,25).year

print(f'''{name} 

and age is {age}''')

name_check = False

if(age == 27):
     name_check = True
     print(name_check)
if(age != 1):
    d=None
    print(d)

height = 5.4

print(f"heignt {height} ")
print(type(height),type(age),type(name_check),type(d))