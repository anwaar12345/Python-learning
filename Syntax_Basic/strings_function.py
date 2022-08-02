paragraph = '''python is a great programming language which is excellent for WEB,AI,DS,Desktop software Development'''

paragraph_new = '''PYTHON is a GREAT programming language which is excellent for WEB,AI,DS,Desktop software Development'''


# print(paragraph[0:])
print("contains : ",paragraph.__contains__('python')) #bool
# print('starts with check : ',paragraph.startswith('python'))

# print("count occurance : ",paragraph.count('great'))

# print('lower case : ',paragraph.lower())

print(''' ******* \nlower case case fold :''',paragraph_new.casefold())

print(''' ******* \nlower case lower :''',paragraph_new.lower())


print(''' ******* \n upper case first letter: ''',paragraph.capitalize())

print(''' ******* \n upper case : ''',paragraph.upper())

print("find letter : ",paragraph.find("python")) #index where found first occurance else -1

print("String Replace",paragraph.replace('python','PHP'))

print("String \t escapes just for \n learning \\new Technology\'s");

if "Python".lower() in paragraph:
    print('yes'.replace('y','Y'));

