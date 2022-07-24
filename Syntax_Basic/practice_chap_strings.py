name = input("Please Enter Your Name: ")

greetings = "Assalam O Alaikum Khush AAM DEED {}".format(name)

greetings_old = "Assalam O Alaikum Khush AAM DEED %s" % (name)

greetings_fway = f"Assalam O Alaikum Khush AAM DEED {name}" 

print("Old Way : ",greetings_old)

print("New Way : ",greetings)

print("fway : ",greetings_fway)