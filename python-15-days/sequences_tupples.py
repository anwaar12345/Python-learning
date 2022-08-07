from distutils.command.config import LANG_EXT
import os
from traceback import print_tb
 
clear = lambda : os.system('clear') 

clear()

tupples = (2,2,2,"users")

# tupples[0] = 22 tupples does not support item assignment 
# but it can have different data types of data
 
print(tupples)

print("****************** tupples functions ****************************")


print("Length of tupples: ",len(tupples))

print("know the occurance of specific number : ",tupples.count(2))

print("find the index of first occurance of specific number : ", tupples.index('users'))


