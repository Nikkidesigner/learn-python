ten_items = "Nikhil the split is important"
print(ten_items)
print("I think these are not ten items")
items = ten_items.split(' ')

more_items = ["six","seven","eight","nine","ten"]

while len(items)!=10:
    new_item = more_items.pop()
    print(f"Adding {new_item}")
    items.append(new_item)
    print("Item added successfully")

print("Final list : ")
print(items)
print(items[1])
print(items[-1])
print(items.pop())
print(' '.join(items))
print('#'.join(items[2:5]))

