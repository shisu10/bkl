# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: 基本路由
"""
from fastapi import APIRouter

from api.login import index, login 
                     #prefix，路由的前缀
Apirouter = APIRouter(prefix="/v1", tags=["api路由"])



@Apirouter.get('/input')
async def home(num: int):
    return {"num": num, "data": [{"num": num, "data": []},{"num": num, "data": []}]}

Apirouter.get("/index", tags=["api路由"], summary="注册接口")(index)

#继承了pydantic basemodel的类被标注到函数又被Apirouter注册路由，
#那fastapi自动获取这个类的schema？
#LOGIN类 -> 注释到login函数 -> 被Apirouter注册路由
Apirouter.post("/login", tags=["api路由"], summary="注册接口")(login)
