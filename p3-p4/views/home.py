# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 8:33 PM
@Author: binkuolo
@Des: views home
"""
from fastapi import Request, Form
from models.base import User

async def home(request: Request, id: str):

    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})


async def reg_page(req: Request):
    """
    注册页面
    :param req:
    :return: html
    """
    return req.app.state.views.TemplateResponse("reg_page.html", {"request": req})

#                               from fastapi import  Form  表单数据
async def result_page(req: Request, username: str = Form(...), password: str = Form(...)):



    add_user = await User().create(username=username, password=password)
    print("插入的自增id", add_user.pk) #pk: primary key
    print("插入的用户名", add_user.username)

    user_list = await User().all().values()


    for user in user_list:
        #  只要{}里面最终是字符串，那么什么对象都可以传
        print(f"用户:{user.get('username')}",user)


    get_user = await User().get_or_none(username=username)
    if not get_user:
        print("")
        return {"info": "没有查询到用户"}
    

    #TemplateResponse就是jinja实例处理模板的方法
    return req.app.state.views.TemplateResponse(
        "reg_result.html", {"request": req, "username":get_user.username, "password": get_user.password})
