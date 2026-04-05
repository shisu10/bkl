from typing import Callable
from fastapi import FastAPI

# def startup(app: FastAPI) -> Callable:

#     async def app_start() -> None:
#         print("启动完毕")
#         await init_db()
#         pass
#     return app_start

def stopping(app: FastAPI) -> Callable:

    async def stop_app() -> None:
        print("停止")
        pass

    return stop_app