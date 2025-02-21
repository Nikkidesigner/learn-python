from dis import dis
from pprint import pprint
import tut_23
def printme():
    print("hello mister how are you ?")

dicto = {
    "color":"red",
    "run":printme
}

print(dicto["color"])
dicto["run"]()
info = dis(tut_23)
pprint(info)