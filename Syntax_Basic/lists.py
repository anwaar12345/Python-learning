tupples = (1,2)
lists = [2,1] #lists are ordered

lists.append(1) #add value to last

print(lists)

lists.pop()

print(lists)

lists.insert(0,12)

print(lists)
for list in lists:
    print("value: ",list)

lists[:0] = [123] # adding value to beginning of list

lists = [43] + lists # adding value to beginning of list

print(lists)

new_list = [1,True,None,"Syed Anwar Ahmed Shah"] #lists can he different data types 

print(new_list[:len(new_list)])

print(new_list[0:])