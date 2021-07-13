"""

    json

    d = {key:value} # dictionary
    d = {1,2,3,4}  # set

    mutable

"""

d = {"name":"royal","role":"admin"} # set
print(d)
print(d["name"])
d["name"]="gabbar"

print(d)

d["email"] = "ram@shyam.com"
d["email1"] = "ram@shyam.com"

print(d)

d.update({"rollNum":420})
print(d)
print("====================")

for k in d:
    print(k,"=>",d[k])
