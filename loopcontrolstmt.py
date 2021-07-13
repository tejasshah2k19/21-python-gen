# break
# continue

"""
for i in range(1,11):
    if i%2 == 0:  #1 2 3
        continue
    print(i)


#output =>  1  3 5 7 9

"""

"""
for i in range(1,6): #1 2
    for j in range(1,i+1): #1 , 1  2
        if i != j:
            continue
        print(j)

#o/p -> 1  2 3 4 5
"""

"""
for i in range(1,6): #1 2 3 4 5
    for j in range(1,i+1): #1 , 1  2 ,1
        if i == j:
            break
        print(j)

 #o/p => 1   1 2
 
 """


for i in range(1,10):
    pass

print("End")

