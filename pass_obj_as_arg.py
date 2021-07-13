class Emp:
    def getData(self):
        self.name = input()
        self.salary = int(input())

    def sum(self,a):
        print(self.salary + a.salary)








emp1 = Emp()
emp2  = Emp()
emp1.getData()
emp2.getData()
emp1.sum(emp2)