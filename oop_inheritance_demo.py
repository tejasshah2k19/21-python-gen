# object of one class can access property of another class
# A --> add() --> object A , B --> objB -> add( )

# Parent - Base - Super
# Child - Derived - Sub

#oop-> five types of inheritance

#   single level [ Empl PartTimeEmpl ]
#   multi level
#   multiple
#   hierarchical
#   hybrid

# code reusability
#Calc add() sub() mul() div()
#SciCalc  sin() sqr() cub()

#facebook --> like()
#post -> like() , photo -> like() , video -> like(),page -> like()->emojis


            #Employee  id , name
#DailyBaseEmpl - wages          FullTimeEmpl - salary


class Employee:
    def getData(self):
        print("enter id and name")
        self.id = input()
        self.name = input()

class FullTimeEmpl(Employee):
    def getData(self):  #over riding
        super().getData() #super() -- access prop from parent
        print("Enter Salary")
        self.salary = int(input())

    def printData(self):
        print("Id : ",self.id)
        print("Name : ",self.name)
        print("Salary : ",self.salary)

class A(FullTimeEmpl):
    pass

fte = FullTimeEmpl()
fte.getData()
fte.printData()













