def sum_local_var(x,y):
    sum = x+y
    return sum

print(sum_local_var(5,3))

a=10
b=20
def sum_global_var():
    sum = a+b
    return sum

print(sum_global_var())