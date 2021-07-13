
# set -=> { } , comma
#uniq
#noindex
#update -> {}
s = {1,2,3,4,5,5 }

d = {"tejas","tejas",12,3,33}

print(s)
print(d)

s = {1,2,3,4,5,5 }
s.update({44})
print(s)
list = [ 11,22,33]
s.update(list)
print(s)


a = {1,2,3,4}
b = {4,5,6}

print(a.union(b)) #no self destructive [ a will not change a remain same ]
print(a) #1 2 3 4
c = a.union(b)
print(c)


a = {1,2,3,4}
b = {4,5,6}
a.update(b)
print(a)

a = {1,2,3,4}
b = {2,3,4,5,6,7}

print(a.intersection(b)) # retunr all common data from a and b , a will remain same
print(a)


a.intersection_update(b) #a will modify and having common data between a and b
print(a)


a = {1,2,3,4,5}

b ={11,22}
c = {3,4}

print(a.issuperset(c)) # superset -> a { a contains all element of c }
print(a.issubset(c)) # c contains all elements of a


a = {1,2,3,4,5}
b = {2,3,4,7,8}
print(a-b)
print(b-a)
print(a.symmetric_difference(b)) # (a-b) U (b-a)










