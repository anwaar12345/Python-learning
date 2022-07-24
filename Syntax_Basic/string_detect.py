from unicodedata import name


name = "shah '' th\'e  great"

print(name.find(''))

print("''" in name)

print(name.__contains__("s"))
name = name.replace("  "," ")
print(name)