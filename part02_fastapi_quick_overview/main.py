from fastapi import FastAPI

app = FastAPI()

# Defining a route
# @app.get means get request
@app.get("/")
def read_root():
    return {
        "message":"you are stronger than you think",
    }

# Get request with path parameter.
@app.get("/item/{item_id}")
def path_parameter(item_id:int):
    item_id += 100
    return {"item_id":item_id}

# To run the fastapi app use:
# fastapi dev main.py (runs the app on it's default port)
# To rhn the app on a custom port use this:
# fastapi dev main.py --port YOUR_PORT