import json
from io import BufferIO

samir={
    'name':'samir',
    'age':25,
    'city':'ktm',
    'country':'nepal'
}

#serialization
json_string=json.dumps(samir)
print(type(json_string))


#deserialization
samir_dict = json.loads(json_string)
print(type(samir_dict))

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return 'woof'
    
puppy = Dog('puppy', 2)
rocky  = Dog('doggy',4)

# puppy_json = json.dumps(puppy)
# print(puppy_json)
# print(type(puppy_json))


# puppy_dict = json.loads(puppy_json)
# print(puppy_dict)
# print(type(puppy_dict))

# dict ={
#     'name':puppy.name,
#     'age':puppy.age
# }

#next way
dict = puppy.__dict__

puppy_json=json.dumps(dict)
print(type(puppy_json))
print(puppy_json)


bytes = puppy_json.encode('utf-8')

buffer = BufferIO()
buffer.write(bytes)
buffer.seek(0)
print(buffer.read())