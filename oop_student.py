class Student:
    def  __init__(self):
        self.maths = 0
        self.eng = 0
        self.sci = 0
        self.perc = 0
        self.grade = ""

    def getMarks(self):
        print("Enter marks for Maths Sci And Eng")
        self.maths = int(input("Maths :"))
        self.sci = int(input("Sci :"))
        self.eng = int(input("Eng :"))

    def printMarks(self):
        print(self.maths,"  ",self.sci,"  ",self.eng)

    def calculateResult(self):
        self.perc = (self.maths+self.sci+self.eng)/3.0;
        if self.perc >= 90 :
            self.grade = "A+"
        elif self.perc >=75:
            self.grade = "B"
        elif self.perc >= 35:
            self.grade = "C"
        else:
            self.grade = "F"

    def printResult(self):
        print(self.maths, "  ", self.sci, "  ", self.eng,"  ",self.perc,"  ",self.grade)


students = []#123 456

while True:
    print("\n1 For Add Student\n2 For Print Results\n0 For exit")
    choice = int(input("Enter choice"))

    if choice == 1:
        s1 = Student() # 456
        s1.getMarks()
        s1.calculateResult()
        students.append(s1)
    elif choice == 2:
        for s in students:
            s.printResult()
    elif choice == 0:
        break
