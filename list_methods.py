list = [ 1,2,3,4,5]

list.reverse()
print(list)

list = [1,12,3,14,15]
list.sort()
print(list)


list = [1,200,23,34,5]
print(max(list))

list.clear() # will remove all the elements from list

print(list) # it will print blank []

#to remove from memory we have del keyword
del list
#print(list)

list = [1,200,23,34,5]

print(list.index(200))
#
# print(list.index(2000)) # run time error -- exception

list.insert(0,500)
print(list)
list = [1,2,3,1,2,3,5,6,7]
print(list.count(3))



x = [1,2,4]
y = x

x[0] = 250




