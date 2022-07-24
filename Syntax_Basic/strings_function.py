paragraph = '''python is a great programming language which is excellent for WEB,AI,DS,Desktop software Development'''

paragraph_new = '''Python is a GREAT programming language which is excellent for WEB,AI,DS,Desktop software Development'''


# print(paragraph[0:])
print("contains : ",paragraph.__contains__('python')) #bool
# print('starts with check : ',paragraph.startswith('python'))

# print("count occurance : ",paragraph.count('great'))

# print('lower case : ',paragraph.lower())

# print("lower case : ",paragraph_new.casefold())

# print("upper case first letter: ",paragraph.capitalize())

print("find letter : ",paragraph.find("python")) #index where found first occurance else -1

print("String Replace",paragraph.replace('python','PHP'))

print("String \t escapes just for \n learning \\new Technology\'s");