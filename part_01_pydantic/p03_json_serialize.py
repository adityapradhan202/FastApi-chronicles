# Here we will convert json structure into an instance of DataModel's class.
# Serialization: It means to convert a complex data structure into a simple one.
# Deserialization: It's the opposite of serialization.

from pydantic import BaseModel
from pydantic import model_validator, ValidationError
import json

# DataModel class
class User(BaseModel):
    name:str
    id:int
    skills:list[str] | None 

    @model_validator(mode='after')
    def validate_name(self):
        if len(self.name) < 3:
            raise ValueError('Name should have more than 3 characters')
        return self
    
# Suppose this is json data
data = '{"name":"Car", "id":4, "skills":["python", "sql"]}'

# Convert the json string into valid python dictionary
data = json.loads(data)

try:
    # This converts a valid python dictionary intoo an instance of data model class
    user = User.model_validate(data)

    print(f"\nDetails of user:")
    print(f"Name: {user.name}")
    print(f"Id: {user.id}")
    print(f"Skills: {user.skills}")
except ValidationError as ve:
    print(f"Validation error: {ve}")


