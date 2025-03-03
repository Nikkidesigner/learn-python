try:
    x= int(input("Enter any number : "))
    y = int(input("Enter the number to divide with : "))
    result = x/y
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"The division of {x} and {y} is : {result}")
