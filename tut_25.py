import tut_24
from pprint import pprint

print("Name : ",tut_24.name)
print("Age : ",tut_24.age)

print("Name using dictionary : ",tut_24.__dict__["name"])
print("Age using dictionary : ",tut_24.__dict__["age"])
with open("dictionaryinfo.txt",'w') as fo:
    info=str(tut_24.__dict__)
    fo.write(info)

tut_24.__dict__["name"] = "Pawar"
print("Name : ",tut_24.name)