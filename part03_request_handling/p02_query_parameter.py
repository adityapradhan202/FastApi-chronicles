# When we declare other parameters in the function, which are not the part of path
# Then those parameters are considered as query parameters
# Note: Test the routes in postman

# Recap:
# While sending a request with query params, the url looks like this:
# localhost:6006?param1=value1&param2=value2 (we use ? and & operator for multiple query parameters)

# Sending requests using query parameters:

from fastapi import FastAPI


app = FastAPI()

horror = ["evil dead rise", "lights out", "incantation"]
action = ["dead pool", "wolverine", "real steel"]

@app.get("/fetch")
def fetch_random_movies(movie_type):
    if movie_type.lower() == "horror":
        return {"type":horror}
    # otherwise return action
    return {"type":action}

# For sending a request with path parameter and multiple query parameter all at once:
# For leveraging pydantic, we dont need to define the base class here
# Fastapi automatically leverages pydantic under the hood

@app.get("/name/{name}")
def show_user_details(name:str, age:int):
    # Now normally string values are passed during the request
    # We will pass age as a string, for example "22"
    # But fastapi uses pydantic under the hood, so it will parse it
    return {
        'user_name':name,
        'age':age, 'type_of_age_variable':str(type(age))
    }


