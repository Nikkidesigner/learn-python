def constructor(color,size):
    print(f">> Constructor color: {color} , Constructor size: {size}")

    #function inside the constructor accessing the constructor values
    def repeater():
        print(f"## Repeater color: {color} , size : {size} ")

    print("<< exit construtor")
    return repeater

blue_xl = constructor("blue","xl")
green_sm = constructor("grenn", "sm")

for i in range(4):
    blue_xl()
    green_sm()