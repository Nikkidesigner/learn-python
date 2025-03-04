import json 

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = {
    "name":"Nikhil",
    "age":27,
    "city":"karad"
}
to_dict = json.loads(x)
to_json = json.dumps(y,indent=4)

print(to_dict)
print(to_dict["name"])
print(to_json)


# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))