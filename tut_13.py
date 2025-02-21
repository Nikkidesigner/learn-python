# convert decimal to binary 

num = int(input("Enter any number : "))


def DeciToBin(num):
    i=0
    set_deci = []
    while num>0:
        set_deci.append(num%2)
        num//=2
        i+=1
    for bit in reversed(set_deci):
        print(bit, end="")

DeciToBin(num)