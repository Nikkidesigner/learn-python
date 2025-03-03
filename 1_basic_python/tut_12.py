 #while loops 
#check armstrong number

num = int(input("Enter any number: "))
temp = num
sum_of_dig=0
count = 0


def FindCount(a):
    # count = 0
    global count
    while a>0:
        a//=10
        count +=1
    return count

power=FindCount(temp)


while num>0:
    sum_of_dig =sum_of_dig +  pow(num%10,power) 
    num=num//10


print("count : ",power, "sum : ", sum_of_dig)


if sum_of_dig==temp:
    print(f"{temp} is an armstrong number with the sum of {sum_of_dig}")
else:
    print(f"{temp} is not an armstrong number")
    
 