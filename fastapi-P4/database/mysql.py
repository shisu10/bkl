# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:15 AM
@Author: binkuolo
@Des: mysql数据库
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os


# 同步函数，不要 async def
def register_mysql(app: FastAPI):
    """
    注册 MySQL 数据库
    """
    # 获取环境变量或使用默认值
    user = os.getenv('BASE_USER', 'root')
    password = os.getenv('BASE_PASSWORD', '123456')
    host = os.getenv('BASE_HOST', '127.0.0.1')
    port = int(os.getenv('BASE_PORT', 3306))
    db = os.getenv('BASE_DB', 'base')
    
    # 构建连接字符串
    db_url = f"mysql://{user}:{password}@{host}:{port}/{db}"
    
    print(f"正在连接数据库: mysql://{user}:***@{host}:{port}/{db}")
    
    register_tortoise(
        app,
        db_url=db_url,
        modules={"models": ["models.base"]},
        generate_schemas=True,  # 自动创建表
        add_exception_handlers=True,
    )
    print("数据库注册成功！")
