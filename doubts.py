# tuple is read only collection or data structure in python
#its a sequential data structure

# we can create tuple usgin ( )

t= (1,2,3,4,5,6,7,8,9,10)
print(t) # print all data from tuple
print(t[0]) #print 0th index
print(t[0:2]) # 0 and 1 index will show
print(t[0:8:2]) # 0 to 8 but increment by 2 => 0 2 4 6 index will show
print(t[0:8:3]) # 0 to 8 but increment by 3 => 0 3 6  index will show
print(t[::3]) # 0 to end but increment by 3 => 0 3 6 9 index will show
print(t[:3]) # 0 to 3 but increment by 1 => 0 1 2   index will show
print(t[::-1])
#once we create tuple we can't modify


########################################################################
#parent method => same method child
# obj.add() # child

# def add():
#  super().add()


# obj.add()

