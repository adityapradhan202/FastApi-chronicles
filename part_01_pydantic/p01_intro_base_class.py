# Introduction to pydantic:
# Pydantic is open source python library which leverages python type hints, to validate incoming data.
# It checks the type of the incoming data, parses the data if needed, and throws proper error when validation fails and parsing is not possible.

# Pydantic is important for fastapi.
# Simplifies data handling, code readability, and helps catch bugs in early development.
# Pydantic is particularly valuable in applications where incorrect malformed data can lead to errors,
# such as API, AI systems processing large and complex data
# Catches bugs earlier, rather than catching it later

# First thing we will learn in pydantic is base model

# By inheriting BaseModel we can make DataModel class
# The DataModel class defines the structure, types, and constraints of the data
# enabling automatic data validation and parsing

from pydantic import BaseModel
from datetime import datetime

# DataModel class
class User(BaseModel):
    # These attrbutes are called Field 
    # These attributes are instance Field class from pydantic
    id: int
    name: str = "John Doe"
    singup_ts: datetime | None # This how wr write optional data types
    tastes: dict[str, int]

# Suppose an external data comes in
external_data = {
    'id':'45', # we are supposed to pass 45 as int
    'name':'Aditya Pradhan',
    'singup_ts':'2026-01-01 10:38',
    'tastes':{'wine':3, 'burger':6, "cheese":9}
}

# To input this data, we will unpack this dictionary and pass the keyword args into the constructor of User class
# And instance will be created

user = User(**external_data)
print(f"Id: {user.id}, Type: {type(user.id)}") # auto parses the str into int
print(f"Name: {user.name}")
print(f"Singup timestamp: {user.singup_ts}")
print(f"Tastes: {user.tastes}")

print()
# We can even simply create an instance of DataModel for another data entry
user2 = User(id=67, name='Rahul', tastes={'pizza':2, 'coke':1}, singup_ts=None)
print(f"Id: {user2.id}, Type: {type(user2.id)}") # auto parses the str into int
print(f"Name: {user2.name}")
print(f"Singup timestamp: {user2.singup_ts}")
print(f"Tastes: {user2.tastes}")

# Important:
# model_dump() method of pydantic
# Converts an instance of our ModelClass into raw python dictionary, preserving the value and type of all the fields
user_dict = user.model_dump()
print(f"\nDictionary representation of model instace: {user_dict}")

# There's another method - model_dump_json() (Upcoming scripts)