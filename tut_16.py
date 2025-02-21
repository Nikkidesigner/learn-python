#Reading files program 

#importing the argument variable
from sys import argv 
#unpacking the variables and storing them into the variables defined
script , filename = argv

#Storing the file as an object into the variable named "text"
text = open(filename)
print(text)

print(f"Your file name is {filename} and its content are :")
#reading the contents of the object text.
print(text.read())

print("Enter another filename which you want to read")
file_again = input(">")
text_again = open(file_again)

print(f"The contents of the another file you selected which is {file_again} are : ")
print(text_again.read())

#close files when you are done with them
text.close()
text_again.close()


#better approach to close the file automatically rather than doing it manually

with open(filename) as file_txt:
    print("After using the with : method ",file_txt.readline())

