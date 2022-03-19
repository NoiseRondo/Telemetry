import json

with open('myfile.json', 'r') as file:
    data = json.load(file)

    print(data)

my_info = {
    'name':'Mir',
    'gender':'Male',
    'status':'Married',
    'age': 18
}

with open('my_info.json', 'w') as j_file:
    json_str = json.dumps(my_info)
    print(json_str, file=j_file)

with open ('myfile.json', 'r') as file:
    data = json.load(file)
    print(data)
