# Why data model classes are nested?
# Ans - To create complex hierarchial data structures
# We have already seen complex nested sort of json data
# To validate such data, we need to nest data model classes

# Here's a simple code example:
from pydantic import BaseModel
import json

class Address(BaseModel):
    street_no:int
    street_name:str
    landmark:str

class User(BaseModel):
    id:int
    name:str
    Address:Address | None # type of Address class or None

# First let's create an object of Address
adrs = Address(street_no=4, street_name='Sabji mandi road', landmark='Apex Gaming Center')
user = User(id=100, name='Aditya Pradhan', Address=adrs)
user_dict = user.model_dump()
print(user_dict, type(user_dict))
# To convert the instance directly into json -> use model_dump_json() method

# This is how we create a json string python dictionary
user_json = json.dumps(user_dict)
print(user_json, type(user_json))