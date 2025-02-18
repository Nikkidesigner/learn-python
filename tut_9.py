"""
Python Binary Data Types
A binary data type in Python is a way to represent 
data as a series of binary digits, which are 0's and
1's. It is like a special language computers
understand to store and process information efficiently.

This type of data is commonly used when dealing with 
things like files, images, or anything that can be 
represented using just two possible values. 
So, instead of using regular numbers or letters, 
binary sequence data types use a combination of 0s 
and 1s to represent information.

Python provides three different ways to represent 
binary data. They are as follows --- 

>> bytes
>> bytearray
>> memoryview

"""
#bytes 
"""
The byte data type in Python represents a sequence of bytes. Each byte is an integer value between 0 and 255. It is commonly used to store binary data, such as images, files, or network packets.

We can create bytes in Python using the built-in bytes() function or by prefixing a sequence of numbers with b.

"""
b1 = bytes([65,66,67,68,69])
print(b1)

#bytearray

"""
The bytearray data type in Python is quite similar to the bytes data type, but with one key difference: it is mutable, meaning you can modify the values stored in it after it is created.

You can create a bytearray using various methods, including by passing an iterable of integers representing byte values, by encoding a string, or by converting an existing bytes or bytearray object. For this, we use bytearray() function.

"""
b2 = bytearray([67,68,69,70,71,72])
print(b2)
