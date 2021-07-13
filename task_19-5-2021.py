print("enter string")
str = input()
#Hello hello Ab ab
#Hello Ab

allWords  = str.split(" ") #Hello hello Ab ab

list = [] #empty Hello

for i in allWords:#Hello hello Ab ab
    duplicate=0
    for j in list:
       if j.lower() == i.lower():
        duplicate=1
    if duplicate == 0:
        list.append(i) #Hello Ab

print(list)