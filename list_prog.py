limit = int(input("Enter Limit"))

list = []

for i in range(0,limit):
    print("Enter number")
    num  = int(input())
    list.append(num)

even=0
odd =0
digit1 =0
digit2 = 0
digit3 = 0

for x in list:
    if x%2 == 0:
        even+=1
    else:
        odd+=1
    if x < 9 and x >= 0:
        digit1+=1
    if x > 9 and x < 100:
        digit2+=1
    if x >= 100 and x <= 999:
        digit3+=1


print(list)
print("Total even = ",even)
print("Total odd = ",odd)

print("Digit1 = ",digit1)
print("Digit2 = ",digit2)
print("Digit3 = ",digit3)


def add(a,b=90):
    pass
add(17)
