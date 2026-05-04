# Main file
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
# Important the scripts from router modules
# Here we will access and use users.router
from routers import users, admin
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="somekey124")

templates = Jinja2Templates("templates")
# Access users/home route
app.include_router(router=users.router, prefix="/users", tags=["Users"]) # tags are used to group and organize routes in swagger UI
app.include_router(router=admin.router, prefix="/admin", tags=["Admin"])

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse(request=request, name="main_home.html", context={}) 
