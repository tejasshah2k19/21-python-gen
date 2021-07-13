"""
error 2
1) compile-time error - syntax  dev
2) run-time error -

exception -> runtime error

exception handling :-

try
hit
throw
handle



"""
class NegNumberException(RuntimeError):
    def __init__(self):
        self.errorReason = "Please Enter Positive numbers..."



try:

    a = int(input("enter number"))
    if a < 0:
        raise NegNumberException

    b = int(input("enter number"))
    c = a/b
    print("div = ",c)
except ValueError:
    print("Please Enter only Integers")
except ZeroDivisionError as z:
     print("Please Do not enter zero")
    #print(z)
except NegNumberException as e:
    print(e.errorReason)
except Exception as e:
    print("Something went wrong please try after sometime....")
    #sendMailToDev(e)
    print(e)
else:
    print("NONE")
finally:
    print("i am always executes....")
    #gc
print("GameOver")

