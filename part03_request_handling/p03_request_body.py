# To send data in the body of the request, we use pydantic BaseModel class

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the data model class
class User(BaseModel):
    name:str
    address:str
    age:int
    occupation:str

# Undefined behavior for sending get request when sending data through body
# Use post, to do it securely
@app.post("/hit_me")
def body_request(user:User):
    # Here the fastapi will read the body of the request as json
    # So we need to send json data while requesting
    # Basically, in postman like tools, we will have to select raw, then Json, to send json data
    # Note: Use double quotes to enclose key-value pairs in the json that u are writing in postman

    # Fastapi uses json encoder under the hood, so it will parse this instance into json
    return user

