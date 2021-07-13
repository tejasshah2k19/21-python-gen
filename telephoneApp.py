
file = open("telephonedata.txt","r")
allLines = file.readlines()
file.close()

usersData = []
durations = []
userUniqNames = set()

for line in allLines:
    record = line.split("|")
    user = {"name":record[0],"clnum":record[1],"duration":record[2],"net":record[3],"st":record[4]}
    usersData.append(user)
    userUniqNames.add(record[0])


print("All user Names")
print(userUniqNames)


while True:
    print("Select one of the following options:\n0 - Exit\n1 - Show users by call duration\n2 - Show users by data usage\n3 - Show users by screen time\n4 - Show all user data")
    choice = int(input())

    if choice == 1:

            print("User  Call Duration")
            for name in userUniqNames:
                totalDuration = 0
                for record in usersData:
                    if name == record.get("name"):
                        totalDuration = totalDuration + float(record.get("duration"))
                #print(name,"  ",round(totalDuration,2))
                durations.append({"name":name,"totalDuration":round( totalDuration,2)})
            #itemgetter->key
            for i in range(0, len(durations)):
                for j in range(i, len(durations) - 1):
                    if durations[j].get("totalDuration") > durations[j + 1].get("totalDuration"):
                        tmp = durations[j]
                        durations[j] = durations[j + 1]
                        durations[j + 1] = tmp

            #print(durations)
            #printMyDictionary(durations)
            for d in durations:
                print(d.get("name"),"      ",d.get("totalDuration"))

    elif choice == 2:
        pass
    elif choice ==3:
        pass
    elif choice == 4:
        pass
    elif choice ==0:
        print("Bye")
        break

