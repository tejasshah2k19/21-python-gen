"""
*
**
***
****
*****
i  	j
1	1
2	12
3	123
4	1234
5	12345
"""




# n=6
# for i in range(1,n):
# 	for j in range(1,i+1):
# 		print("*",end="")
# 	print("")


# 1
# 12
# 123
# 1234
# 12345



# n=6
# for i in range(1,n):
# 	for j in range(1,i+1):
# 		print(j,end="")
# 	print("")




# 1
# 22
# 333
# 4444
# 55555

# n=6
# for i in range(1,n):
# 	for j in range(1,i+1):
# 		print(i,end="")
# 	print("")

#     *
#    **
#   ***
#  ****
# *****





# n=6
# for i in range(1,n):
# 	for s in range(n,i,-1):
# 		print(" ",end="")
# 	for j in range(1,i+1):
# 		print("*",end="")
# 	print("")



#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n=6
for i in range(1,n):
	for s in range(n,i,-1):
		print(" ",end="")
	for j in range(1,i+1):
		print("* ",end="")
	print("")










