from ast import Try
import os

clear = lambda : os.system('clear')
clear()
lists = [1,2,2,3,"system",True]
lists[3] = "new it supports item assignment index vise"
print('List can contain \n different data types of data \n and can contain dupplicated values \n',lists)

print('****************** Lists Functions **********************')

lists.append(1)
list_copy = lists.copy()
lists.extend(list_copy)
print(lists)


lists.remove(1)

print(lists)
lists.pop(0)
print(lists)

listed = [2,3,4,0]
listed.sort()

print(lists)
