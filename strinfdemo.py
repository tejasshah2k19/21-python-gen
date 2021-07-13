#string --- collection of characters
# its an immutable
# you can access individual characters using index
# both the index can be possible forward and backward
# forward index starts with 0 and ends with size-1
# backward index starts with -1 and ends with -size
# you can also use slicing





name="royal" #name-> string
print(name)
name = name.upper() # all alphabets are gonna upper case capital
print(name) # ROYAL



# immutable


print(name[0])
print(name[0:4]) # 0 inclusive 4 exclusive so 0 1 2 3 taken
print(name[0:3])
print(name[:])
print(name[:-1])
print(name[::])
print(name[::-1])
print(name[::2])
print(name[::-2])

