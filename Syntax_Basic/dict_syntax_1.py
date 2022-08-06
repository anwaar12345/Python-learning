import os
clear = lambda : os.system('clear')
clear()
person_details = {
    "Name" : "Syed Anwar Ahmed Shah",
    "Son_of" : "Syed Zia Hussain Shah",
    "Age" : 27,
    "Designation" : "BackEnd Software Engineer",
    "Skills" : {
        "Languages" : ['PHP','Python','Javascript'],
        "Framework" : ["Laravel","DJANGO"]
    },
}

print(person_details['Skills'])

for i,v in person_details.items():
    print(f"{i.replace('_',' ')} : {v}") 