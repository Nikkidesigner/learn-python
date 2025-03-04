import json

dictionary = {
    "name":"nikhil",
    "age": 21,
    "city":"karad"
}

to_json = json.dumps(dictionary,indent = 3)

with open("sample_1.json","w") as file:
    file.write(to_json)

with open("sanple_2.json","w") as file_1:
    json.dump(dictionary, file_1)