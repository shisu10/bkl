# -*- coding:utf-8 -*-
"""
@Time : 2022/4/23 11:46 AM
@Author: binkuolo
@Des: 视图路由
"""
from fastapi import APIRouter
from starlette.responses import HTMLResponse

from views.home import home, result_page, reg_page

ViewsRouter = APIRouter()

# response_class=HTMLResponse指定路由返回的内容按 HTML 格式处理，浏览器会直接渲染成网页。
# 不指定默认为json
ViewsRouter.get("/items/{id}", response_class=HTMLResponse)(home)
ViewsRouter.get("/reg", response_class=HTMLResponse)(reg_page)
ViewsRouter.post("/reg/form", response_class=HTMLResponse)(result_page)


