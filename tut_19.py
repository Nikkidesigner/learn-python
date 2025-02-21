with  open("seekfile.txt",'w+') as fo:
    fo.write("change me : this is the new file for testing seek operations")
    # Move the file pointer to the beginning before reading
    fo.seek(0)
    original = fo.read()
    print("Original data:", original)
    fo.seek(7,0)
    data=fo.read(2)
    print(f"The text to be replaced is : {data}")
    fo.seek(7,0)
    change = input("Enter the text to be replaced:")
    fo.write(change)

with open("seekfile.txt",'r') as fo:
    data = fo.read()
    print(data)

