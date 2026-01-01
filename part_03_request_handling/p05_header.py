# Sending data in header
# The process is very similar to what we have done in form submissio

from fastapi import FastAPI
from fastapi import Header
from typing import Annotated

app = FastAPI()

# While testing the route, send data in headers
@app.post("/api_auth")
def api_key_auth(apikey:Annotated[str | None, Header()]):
    if apikey is not None:
        if apikey.lower() == "badmeetsevil":
            return {
                "status":"access granted"
            }
        else:
            return{
                "status":"access denied"
            }
            
    return {
        "message":"did not get the api key",
        "status":"verifieds"
    }