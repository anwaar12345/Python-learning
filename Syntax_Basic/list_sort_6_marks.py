import os
import os

clear = lambda : os.system('clear')
clear()
marks = []
for i in range(0,6):
   marks.append(int(input("please Enter Marks: ")))

marks.sort()

print('Marks Sorted: \n \t',marks)


