import os
option = int(input('''please enter option 1 for dir 2 for cwd:'''))

if(option == 1):
    print("the current dir "+ os.getcwd())

elif(option == 2):
    print(os.listdir()[1]) #returns array of directories

else: 
    print('wrong')