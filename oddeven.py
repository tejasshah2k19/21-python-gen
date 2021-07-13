
numbers = open("numbers.txt","w")
for i in range(1,6):
    num = input("Enter number")
    numbers.write(num+"\n")
numbers.close()

odd = open("odd.txt","w")
even = open("even.txt","w")
numbers = open("numbers.txt","r")

allNumbers = numbers.readlines()

for line in allNumbers:
    if(int(line) % 2 == 0):
           even.write(line)
    else:
        odd.write(line)

numbers.close()
odd.close()
even.close()

odd = open("odd.txt","r")
numbers  = open("numbers.txt","r")
even = open("even.txt","r")


print(numbers.readlines())
print(odd.readlines())
print(even.readlines())






