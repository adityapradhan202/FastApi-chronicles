from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from typing import Annotated
from fastapi import Form

app = FastAPI()

# Routes here
templates = Jinja2Templates(directory='templates')

item_list = ["Chichek Kali Mirch", "Pyaaz Parantha", "Paneer Parantha"]

@app.get("/")
def home_page(request:Request):
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"profession":"AI Engineer"}
    )

@app.post("/submit-form")
async def form_submission(name:Annotated[str, Form()], profession:Annotated[str, Form()],
                    request:Request):
    """Takes form data"""

    if name == "Aditya Pradhan":
        return templates.TemplateResponse(name="index.html", request=request,
                                          context={"profession":"Senior AI Engineer"})
    elif name == "Rahul Pradhan":
        return templates.TemplateResponse(
            name="second.html", request=request, context={"item_list":item_list}
        )
    else:
        print(f"Details from the form:")
        print(f"Name: {name}, Profession: {profession}")
        return {"name":name, "profession":profession}