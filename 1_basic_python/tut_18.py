#writing into a file 
from sys import argv
script , filename  = argv

with  open(filename,"w") as file_txt: 
    content = input(f"Enter the content to write in {filename} : \n")
    file_txt.write(content)
    file_txt.write("\n")
    print("File written successfully !")



  # truncating the file : goodbye 
print("Truncating the file ..........")
with open(filename,"w") as file_txt:
     file_txt.truncate()



#appending to an existing file :
file_txt= open(filename,"a")
content = input(f"Enter the content to append in {filename} : \n")
file_txt.write(content)
print("\n File written successfully !")


#closing the object to save the space 
file_txt.close()
