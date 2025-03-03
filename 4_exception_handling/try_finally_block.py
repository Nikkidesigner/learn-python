try:
    x = int(input("Enter any number : "))
    result = x*x
    flag=0
except ValueError:
    flag=1
    print("Enter the correct value (any integer).")
finally:
    if flag==0:
        print(f"The square of {x} is {result}")
    else:
        print("Program ended with exceptions.")