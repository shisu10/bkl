# -*- coding:utf-8 -*-
"""
@Time : 2022/4/25 2:37 PM
@Author: binkuolo
@Des: test redis
"""

from core.Response import success
from fastapi import Depends, Request
from database.redis import sys_cache
from aioredis import Redis


#事件启动时：在应用启动事件中创建全局连接池并存入 app.state，所有请求共用同一实例。
async def test_my_redis(req: Request):
    # 连接池放在request
    value = await req.app.state.cache.get("today")

    return success(msg="test_my_redis", data=[value])


#依赖注入：在依赖函数中检查并复用全局单例，避免每个请求重复创建。
#当前代码没有用到这种检查并复用全局单例这种方法，只是重复调用池
async def test_my_redis_depends(today: int, cache: Redis = Depends(sys_cache)):
    # 连接池放在依赖注入
    # await cache.set(name="today", value=today)
    await cache.set(name="ex_today", value=today, ex=60)
    # value = await cache.get("today")
    return success(msg=f"今天是{today}号", data=[])
