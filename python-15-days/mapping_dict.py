from ast import Try
import os

clear = lambda : os.system('clear')
clear()

bio_data = {
  "name" : "Syed Anwar Ahmed Shah",
  "Son_of" : "Syed Zia Hussain Shah",
  "age" : 27,
  "Qualification" : "BSSE",
  "Profession" : "Software Engineer",
  "Specialization" : "Backend Engineering",
  "Skills" : {
    "languages" : "PHP | Javascript | Python",
    "Database" :  "MYSQL | RDBMS",
    "Frameworks" : "Laravel | Django(Learning) | NODEJS(To Learn)"
  }
}

for i,v in bio_data.items(): 
    print(f"{i.replace('_',' ').upper()} : ")
    if(type(v) == str) :
        print(f"{v.upper()}")
    elif(type(v) == dict):
        for s,t in v.items():
         print(f"{s.replace('_',' ').upper()} : ")
         print(t)

