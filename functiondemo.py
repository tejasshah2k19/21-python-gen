# modular
# reuse
# recursion
#collection of instructions which will execute line by line and give some output.


#define
#no return no argument
def add():
    print("Enter two numbers")
    a = int(input())
    b = int(input())
    c = a+b
    print("addition = ",c)

#no return type with argument
def sub(a,b):
    c = a-b
    print("subtraction = ",c)

#return - no argument
def mul():
    a = int(input("Enter a number"))
    b = int(input("Enter a number"))
    c = a*b
    return c

#return - with argument
def div(a,b):
    c=a/b
    return c


def calc():
    add()
    sub(10,2)
    ans = mul()
    print("mul = ",ans)
    print("div = ",div(10,2))

#calling
#add()
#sub(5,2)
#calc()

def abcd(a=12,b=23):
    print(a)
    print(b)

abcd()
print("===")
abcd(50)
print("===")

def currencyConvertor(amount=10,currencyName="dollar"):
    if currencyName == "dollar":
        return amount * 75,"INR"
    elif currencyName == "euro":
        return  amount * 90,"INR"


y=currencyConvertor(10,"dollar")
x,z=currencyConvertor(10,"dollar") # x = 750 y = "INR"

# (750,"INR") => tuple
# [750,"INR"] => list
#750,"INR"

print(y[0]) #750
print(y[1]) # INR
for data in y:
    print(data)

print(currencyConvertor(10,"euro"))
print(currencyConvertor(100))

#set dictionary list ""tuple""
