from fastapi import APIRouter
from starlette.responses import HTMLResponse

from views.home import home

ViewRouter = APIRouter()

ViewRouter.get("/item{id}",response_class=HTMLResponse)(home)

