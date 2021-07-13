
name = "royal"
#function
print(name)
print(len(name))#5

#methods

print(name.upper())
print(name)# royal

print(name.lower())

name ="royal education"
print(name.capitalize()) #royal education => Royal education
print(name.title())  # Royal Education
print(name.isalpha()) #False ->  check all characters must be alphabets
name ="royal"
print(name.isalpha())
print(name.isdigit())
name="123"
print(name.isdigit())

name ="jony jony yes papa"
print(name.count("j"))
print(name.count("jony"))

name = "admin"
name2 = "royal"
name3 = "royal"
print(name == name2)
print(name2 == name3)

name ="         jony       "
print(name)
print(name.strip()) # space


name ="#####jony@@@@@@"
print(name)
print(name.strip("#").strip("@")) # space


name ="######jony####"
print(name)
print(name.lstrip("#")) #
print(name.rstrip("#")) #


name ="royal education education"
print(name.endswith("edu")) # False
print(name.endswith("ion"))
print("royal education".endswith("ion"))

name = "jony royal jony royal"
print(name.index("royal")) # 0













