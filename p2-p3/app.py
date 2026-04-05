# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: binkuolo
@Des: app运行时文件
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from config import settings
from fastapi.staticfiles import StaticFiles
from core.Router import AllRouter
from core.Events import startup, stopping
from core.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, UnicornException
from core.Middleware import Middleware
from fastapi.templating import Jinja2Templates

application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME
    )


# 事件监听
application.add_event_handler("startup", startup(application))
application.add_event_handler("shutdown", stopping(application))


# 异常错误处理
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http422_error_handler)
application.add_exception_handler(UnicornException, unicorn_exception_handler)

# 路由
application.include_router(AllRouter)

# 中间件
application.add_middleware(Middleware)
application.add_middleware(
    SessionMiddleware,
    secret_key="session",
    session_cookie="f_id",
    # max_age=4
)
application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)

# 静态资源目录

# mount 注册一个完整的应用，负责处理某个路径前缀下的所有请求。
# router.get() 注册一个具体的函数，只处理某个精确路径的单一 HTTP 方法。

# mount 是把一个能处理请求的"应用"挂到某个 URL 路径上，让该应用接管这个路径下的所有访问。
# 所有被mount的（ASGI）应用都通过send反馈,被框架（异步）调用后，通过send反馈
application.mount('/static', StaticFiles(directory=os.path.join(os.getcwd(), "static")))
# state存储内部共享数据到应用实例中(python层面，不能被mount)
# .state把python对象存储成state的属性
application.state.views = Jinja2Templates(directory=settings.TEMPLATE_DIR)

app = application
