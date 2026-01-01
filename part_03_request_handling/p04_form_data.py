# Recap for Annotated class:
# Annotated class is used to add the type as well as the meta data.
# For example Annotated[int, "must pe positive"]
# Example: Annotated[int, Form()] -> int and sent through Form, Form() class is of fastapi

from typing import Annotated
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

# Method 1. Using Annotated class
# Test the route by sending form data or url-encoded form data with postman
# Async because form submission in fastapi is considered async in nature
@app.post("/send_form_data")
async def form_data_display(name:Annotated[str, Form()], age:Annotated[int, Form()]):
    return {
        "name":name,
        "age":age
    }

# Method 2. Using pydantic model for 
class FormData(BaseModel):
    username:str
    age:int

@app.post("/send_data")
async def form_data(data:Annotated[FormData, Form()]):
    return {
        "username":data.username,
        "age":data.age
    }