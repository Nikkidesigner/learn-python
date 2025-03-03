#simple tuple

tuple_1 = (2023, "nikhil", 44.4, 3+5j)
print(tuple_1)
print(type(tuple_1))

#tuples can contain list
 
tuple_2= ([1,2,3], 2, 3.4, (1,3,5), "Nikhil")
print(tuple_2)

#operations on tuples 

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples