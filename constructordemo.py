class User:
    #
    # def __init__(self):
    #      self.name = "admin" #instance variable
    #      self.email = "admin@gmail.com"
    #      print("this is default const...")

    def __init__(self,name,email):
        self.name = name
        self.email = email
        print("para..const")

    def printData(self):
        print(self.name)
        print(self.email)

#
# u = User()
# print(u.name)
# print(u.email)
u1 = User("ram","ram@sita.com")
print("line 22 ->  ",u1.name)
u1.name = "jaiho"
print("line 24 => ",u1.name)
print(u1.email)
u1.printData()


u2 = User("ravan","ravan@sita.com")
print(u2.name)
print(u2.email)
u2.printData()

#User.printData(u1) # new

print("game over")


