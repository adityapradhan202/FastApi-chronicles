# Path parameter
# Sending requests using path parameters
# Note: Test the routes in postman

from fastapi import FastAPI

app = FastAPI()

# Sending a get request with two path parameters
@app.get("/sum/{n1}/{n2}")
def sum_two_nums(n1:int, n2:int):
    # We can access the path parameters, by using the same variables as function paramters
    sum = n1 + n2
    return {
        "sum":sum
    }

# Sending a post request with one path parameter
@app.post("/send_data/{name}")
def user_name_display(name):
    return {
        "message":"received your name",
        "name":name
    }