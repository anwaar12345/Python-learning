import os
clear = lambda: os.system('clear')
clear()
#it will modify orignal list and cant be re-assign it will return none
numbers = [1,10,2,3,5,4,6,7,8,9]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(122)
print('append',numbers)
numbers.insert(2,111) #inserts at given index
print(numbers)
numbers_copy = numbers.copy( );
print("copy : ",numbers_copy)
numbers.extend(numbers_copy) #will merge lists into orignal
print('extended: ',numbers)
print("count: ",len(numbers))
numbers.pop(0) # if we give index it will pop else if not index will pop last index
print("pop number from list: ",numbers)
numbers.pop() # if we give index it will pop else if not index will pop last index
print(numbers)
numbers.remove(6) 
print('remove: ',numbers)