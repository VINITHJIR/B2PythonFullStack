#convert json to python dictionary

import json
data = '{"idly" : 10 , "dosa" : 20 , "vada" : 15 , "poori" : 25}'

result = json.loads(data)
print(result)

#python object to json

import json

menu = {
    "idly": 10,
    "dosa": 20,
    "vada": 15,
    "poori": 25
}

json_data = json.dumps(menu)

print(json_data)
print(type(json_data))
