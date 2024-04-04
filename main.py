import json


file_name = "maamoun_json.json"
with open(file_name, "r") as f:
    data = json.load(f)

# print(type(data))
# print(type(data.get("friends")))

################################

class Person:
    def __init__(self, name, age) -> None:
        self.name, self.age = name, age

p1 = Person("Maamoun", 30)

# object info as dictionary data structure
# p1.__dict__

# with open("p1.json", "w") as f:
#     json.dump(p1.__dict__, f, indent=4)

##################################    

import requests

req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# print(type(req.text))

data = json.loads(req.text)
# print(data)
# print(type(data))

str_json = json.dumps(data)
print(str_json)
print(type(str_json))
