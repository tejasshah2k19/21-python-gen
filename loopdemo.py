"""
i=100
while i<=10:
	print(i)
	i=i+1
	#i+=1
print("out of while") 
"""

limit =  int(input("enter limit"))

for i in range(1,limit+1):
	print(i)

for i in range(1,limit+1,2): # this will increment by 2 
	print(i)	

#reverse loop 
for i in range(limit,0,-1): # this will decrease by 1 
	print(i)	











