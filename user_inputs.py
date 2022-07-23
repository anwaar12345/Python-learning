print(''' ****** Personal Information Form ******** ''')
name = input("Please Enter Name: ")
age = input("Please Enter Age: ")
designation = input("Please Enter Designation: ")
specialization = input("Please Enter Specialization: ")
skills  = input("Please Enter Skils: ")
years_of_experience = input("Please Enter professional experience: ")

# input() also returns string


print(f'''
******** Personal Information ********
Name: {name}
Age: {age}
Designation: {designation}
Skills: {skills}
Professional Experience: {years_of_experience} 
 ''')