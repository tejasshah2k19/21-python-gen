
contacts = []  # [{"name":"tejas","contact":"2323"},{},{}]

#global


def addContact():
    print("your choice ", choice)
    print("Enter name and contact number")
    name = input()
    contact = input()
    c = {"name": name, "contact": contact}
    contacts.append(c)

def displayContacts():
    print("************ALL CONTACTS***************")
    print("Name     Contact")
    for c in contacts:
        print(c["name"],"   ",c["contact"])

def  searchContact():
      pass


choice = 0
while True:
    print("1 For add contact")
    print("2 For add search contact")
    print("3 For list all contacts")
    print("4 For remove contact")
    print("5 For exit ")
    choice = int(input("Enter choice"))

    if choice == 1:
        addContact()

    elif choice ==2:
        searchContact()

    elif choice ==3:
        print("your choice ",choice)
        displayContacts()
    elif choice==4:
        print("your choice ",choice)
    elif choice==5:
        exit(0)
    else:
        print("Invalid Option Please Try again!!!!")
