from api.Base import Apirouter
from views.Base import ViewRouter
from fastapi import APIRouter

AllRouter = APIRouter()

AllRouter.include_router(ViewRouter)
AllRouter.include_router(Apirouter)