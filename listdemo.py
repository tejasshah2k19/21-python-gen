# mutable
# index
# slicing
# index starts with 0 and ends with len-1
# it can have n number of data with mixtures of data type
# operator
# + {merge} , * {replicate} , relational operator
# list is a part of sequence data type of python {6}
# in not in
list = [ ]

list.append(12)
list.append(32)
list.append(33)
list.append(52)
list.append("royal")
list.append("education")

print(list) # full list

for data in list:
    print(data)


x = [1,2,3]
print(x*3)

x = [1,2,3]
y = [4,5,6]
z = x+y # 1  2 3 4 5 6
print(z)

x = [1000,12]
y = [1000,12]

print(x > y )

x = [11,22,33]

print(300 in x) # False
print(300 not in x)# True

