#simple list

list_1= [2023,"python", 3.11, 5+6j, 1.23E-4]
type([2023,"python", 3.11, 5+6j, 1.23E-4])
print(list_1)
print(type(list_1))

# nested list

list_2=[[1, 2, 3],[1.2, 2.3, 4.4],["A","B","C"]]
print(list_2)
print(type(list_2))


#list operations
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists