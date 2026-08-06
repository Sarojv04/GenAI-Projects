from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

person_info: Person = {'name' : 'Ram', 'age':28}

print(person_info)
