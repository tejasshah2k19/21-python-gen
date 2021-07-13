def add(a,b):
    print("A = ",a)
    print("B = ",b)

def sum(p,*data):
    print("==========")
    print(p)
    print(data) #1,
    ans = 0
    for d in data:
        ans = ans + d
    print("sum = ",ans)
    print("===========")

add(b=100,a=200)
sum(1,2,3) #6
sum(12,23,34,34) #
sum(1) # 1
sum(1,2,3,4,5,6,7,8,9,10) #

print("Enter limit")
limit = int(input()) # 5

for i in range(0,limit):
    print("Enter a number ")
    x = int(input())




