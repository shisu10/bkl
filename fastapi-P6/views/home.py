# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 8:33 PM
@Author: binkuolo
@Des: views home
"""
from fastapi import Request, Form, Cookie
from models.base import User
from typing import Optional
"""
application.add_middleware(SessionMiddleware,...)
app注册了SessionMiddleware，用Cookie()获取cookie时自动获取session
request是独立的，所以cookie和session不会混淆
"""

"""
    点对点的连接靠tcp(ip,端口)
    cookie是某个对话的钥匙,浏览器记录cookie对应的网址域名
"""

async def home(request: Request, session_id: Optional[str] = Cookie(None)):
    # return templates.get_template("index.html").render({"request": request, "id": id})
    cookie = session_id
    session = request.session.get("session")
    page_data = {
        "cookie": cookie,
        "session": session
    }
    # request.session.setdefault("55555", "hdaldais")
    return request.app.state.views.TemplateResponse("index.html", {"request": request, **page_data})
                                                                                       #**把键值对解包到外层字典

async def reg_page(req: Request):
    """
    注册页面
    :param req:
    :return: html
    """
    return req.app.state.views.TemplateResponse("reg_page.html", {"request": req})

    """
        ...是Python的Ellipsis单例对象，FastAPI用它标记字段为必需

        username: str = Form(...)
        从表单中获取name="username"的输入框的值，并赋值给变量username
    """
async def result_page(req: Request, username: str = Form(...), password: str = Form(...)):
    """
    注册结果页面
    :param password: str
    :param username: str
    :param req:
    :return: html
    """

    add_user = await User().create(username=username, password=password)
    print("插入的自增ID", add_user.pk)
    print("插入的用户名", add_user.username)

    user_list = await User().all().values()
    # 打印查询结果
    for user in user_list:
        print(f"用户:{user.get('username')}", user)

    # 获取当前创建的用户
    get_user = await User().get_or_none(username=username)
    if not get_user:
        print("")
        return {"info": "没有查询到用户"}

    return req.app.state.views.TemplateResponse(
        "reg_result.html", {"request": req, "username": get_user.username, "password": get_user.password})
