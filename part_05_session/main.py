from fastapi import FastAPI, Request
from fastapi import Form
from typing import Annotated
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI()
# secret key is important to prevent attackers
# This secret key helps us to reject any cookies that do not match the signature against the secret_key
app.add_middleware(SessionMiddleware, secret_key='mysession_secretkey556')
templates = Jinja2Templates(directory="templates")

# Home page
@app.get("/")
def homepage(request:Request):
    return templates.TemplateResponse(request=request, name="home.html", context={})

@app.post("/login")
def verify_user(request:Request, username:Annotated[str, Form()], password:Annotated[str, Form()]):
    """Verify the user"""
    if username == "admin" and password == "admin123":
        request.session["username"] = "admin"
        return RedirectResponse(url="logged-in", status_code=303) # Redirect to the logged-in page
    else:
        print("Invalid creds!")
        return templates.TemplateResponse(request=request, name="home.html", context={})
    
@app.get("/logged-in")
def logged_in(request:Request):
    if request.session.get("username"):
        return templates.TemplateResponse(request=request, name="logged_in.html", context={
            "username":request.session.get("username")
        })
    else:
        print("User not in the session! But tried to log in!")
    
@app.post("/logout")
def logout(request:Request):
    if request.session.get("username"):
        request.session.clear()
        return RedirectResponse(url="/", status_code=303)
    else:
        return RedirectResponse(url="/", status_code=303)
    

    