class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def print_info(self):
        print(f"Hello {self.name}, welcome to Python.\nYour gender is {self.gender} and your age is {self.age}.\nThank you.\n")

# Creating 1,000 Person objects and storing them in a list
list1 = []

for i in range(10):  # 1000 people
    obj = Person("Nikhil", "male", 22)
    list1.append(obj)  # Use append() to add objects to the list

# Printing the details of all 1000 people
for person in list1:
    person.print_info()  # Call the method for each object
