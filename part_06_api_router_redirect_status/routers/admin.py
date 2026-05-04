from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import Annotated
from fastapi import Form

router = APIRouter()
templates = Jinja2Templates("templates")

# Make sure to add the SessionMiddleware to the main app
# Note - Important concept: Use 303 status code after POST form submission
# 303 forces GET method, and status code
# 303 means a request has been successfully processed (Either POST or PUT method) and then redirects to a route which requires GET method

# 302 MAY preserves the same method (depend on the browser) 
# 307 always preserves the method. Suppose we did a forms submission with post, and then redirect with 307, that will hit back the request with POST even if it is supposed to be a GET
@router.get("/home")
def admin_home(request:Request):
    return templates.TemplateResponse(name="admin_home.html", request=request, context={})

@router.post("/login")
def admin_login(request:Request, username:Annotated[str, Form()], password:Annotated[str, Form()]):
    if username == "admin" and password == "admin123":
        print("--> User verified!")
        request.session["username"] = username # Add admin to the session
        username = request.session.get("username")
        return RedirectResponse(url="/admin/secret", status_code=303)
    else:
        print("Invalid credentials")
        return RedirectResponse(url="/", status_code=303)
    
@router.get("/secret")
def admin_secret(request:Request):
    if request.session.get("username"):
        return templates.TemplateResponse(request=request, name="admin_secret.html", context={
            "username":request.session.get("username")
        })
    else:
        return RedirectResponse("/admin/home", status_code=303)
    
@router.post("/logout")
def admin_logout(request:Request):

    print("-> Admin has been remnoved from the session")
    request.session.clear() # Remove admin from the session
    return RedirectResponse("/admin/home", status_code=303)
    




