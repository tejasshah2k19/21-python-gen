#file handling

"""

#fp = open("demo.py","w")
fp = open("first.py","r")

#data = fp.read() # read entire content of file and store into given variable
#data = fp.read(20)
#data = fp.readlines()

data = fp.readline(100) #it will read first line -- entire
print("1 => ",data)
print("1 => ",data[5:12])
print("1 => ",data)


data = fp.readline(5) #it will read second line -- max 5 records
print("2 => ",data)


#print(data[3]) # index 0

fp.close()
"""


"""
    w  - write [ file overwrite ] 
    a  - append  [ append ] 
"""

"""
fp = open("mydata.txt","r")
data  = fp.readlines() #tejas royal python
data.pop(1) #this will remove royal
print(data) # tejas python
fp.close()

fp = open("mydata.txt","w")
fp.writelines(data)# tejas python
fp.close()

"""

import os

#remove file
#os.remove("mydata.txt")

""" 
if os.path.exists("mydata.txt"):
    os.remove("mydata.txt")
else:
    print("File not found...")
"""

#os.mkdir("demo")
#os.rmdir("demo") #folder must be empty

#directory listing

dir = os.listdir()
print(dir)

dir = os.listdir("d:\\python\\")
print(dir)













