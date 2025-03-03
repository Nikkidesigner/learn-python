fruit = [
 ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'],
 ['Pears', 2, 'A'], ['Grapes', 14, 'UR']]

cars = [
 ['Cadillac', ['Black', 'Big', 34500]],
 ['Corvette', ['Red', 'Little', 1000000]],
 ['Ford', ['Blue', 'Medium', 1234]],
 ['BMW', ['White', 'Baby', 7890]]
 ]

languages = [
 ['Python', ['Slow', ['Terrible', 'Mush']]],
 ['JavaSCript', ['Moderate', ['Alright', 'Bizarre']]],
 ['Perl6', ['Moderate', ['Fun', 'Weird']]],
 ['C', ['Fast', ['Annoying', 'Dangerous']]],
 ['Forth', ['Fast', ['Fun', 'Difficult']]],
]

print(fruit[0][1]) #12
print(fruit[0][2]) #AAA
print(fruit[2][1]) #2

print(cars[0][1][1]) #Big
print(cars[1][1][0]) #red
print(cars[1][1][1]) #little

numbers = [10, 20, 30, 40]
numbers.append(50)  # Adds 50 to the list
numbers.remove(20)  # Removes the first occurrence of 20
numbers.insert(1, 15)  # Inserts 15 at index 1
numbers.reverse()  # Reverses the list


print(numbers)