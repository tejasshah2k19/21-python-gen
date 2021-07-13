list = [1,2,3,55,66,22,33]

print(len(list)) # 7

#del list  #del is a keyword to remove any object from memory

print("max = >  ",max(list))


#method

list.append(1200)
print(list)

#sort
list.sort() # asc  mutable
print(list)
list.reverse()
print(list)

list = [11,22,33,44]
list.remove(22) # remove method will remove element from list
print(list)

list.pop() # top of the stack -- LIFO
print(list)

list.pop(0) # index
print(list)

list = [1,2,3,33,44,55,55,33]
print( list.count(33))

list = [1,2,3,33]
list.append(55) # last
list.insert(0,-1) #-1 1 2 3 33
print(list)

list.insert(1,"royal")
print(list)








