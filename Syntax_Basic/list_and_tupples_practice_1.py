import os
clear = lambda : os.system('clear')
clear()

total_fruits = int(input('How many Fruits you want to store: '))

fruits_list = []

for total_fruit in range(0,total_fruits):
    fruits_list.append(input('name: ').capitalize())

print('list of fruits: ',fruits_list)    