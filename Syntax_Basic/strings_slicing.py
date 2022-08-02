name  = "shah"
greetings = 'Assalam O Alaikum'
print(len(name))
print(type(name))
print(greetings + " " + name)

print('strings ',name[0:])
if "shah" in name:
    print(name[0:]) # shah : right py hu ti  us number sy last tk ly ga wrna agr left py hu tu 0 sy us char tk ly ga jo index dia hy 


print(name[2:]) # ah    

print(name[-4:])


#character skipping third argument will skipp every 2nd char

print("slicing skip every two : ",name[0:4:2])
print('',name[0::2])
print("string get from 0 t0 4 : ",name[:4])
print("string get after 4 : ",name[2:])
print("string get after 2 to last element: ",name[2:-1])
print("string get after : ",name[-3:-1])

print(name[:2])