# Deserialization: Transforming simpler data structure back to it's original form
# We will conver the DataModel's class instance back to json string

from pydantic import BaseModel

class Employee(BaseModel):
    id:int
    name:str
    skills:list[str]

emp = Employee(id=34, name='Joe', skills=["Python", "Langchain", "Langraph", "Transformers"])
# We saw a method .model_dump() -> converts an instance into valid python dictionary
# Now we will use model_dump_json() -> converts an instance into valid json string

json_emp = emp.model_dump_json()
print(json_emp)
print(f"Type: {type(json_emp)}") # This will be a json string