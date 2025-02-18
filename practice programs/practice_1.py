a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))

def Add(a,b):
    sum = a+b
    return sum


def Sub(a,b):
    if(a>b):
        return a-b
    else:
        return b-a

def Div(a,b):
    return a/b


def Mul(a,b):
    return a*b


print(f"Addition of {a} and {b} is : ", Add(a,b))
print(f"Substraction of {a} and {b} is : ",Sub(a,b))
print(f"Division of {a} and {b} is : ",Div(a,b))
print(f"Multiplication of {a} and {b} is : ",Mul(a,b))

