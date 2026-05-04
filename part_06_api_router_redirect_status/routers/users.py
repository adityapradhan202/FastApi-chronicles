from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter() # Name the instance router
templates = Jinja2Templates("templates")

@router.get("/home")
def user_home(request:Request):
    """Home page for the users"""
    return templates.TemplateResponse(request=request, name="users_home.html", context={})

