from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestErrorModel
from pydantic import ValidationError



async def http_error_handler(_: Request, exc: HTTPException):


    return JSONResponse({
        "code": exc.status_code,
        "message": exc.detail,
        "data": exc.detail
    }, status_code=exc.status_code)

class UnicornException(Exception):

    def __init__(self, code, errmsg, data=None):


        if data is None:
            data = {}
        self.code = code
        self.errmsg = errmsg
        self.data = data

async def unicorn_exception_handler(_: Request, exc: UnicornException):

    return JSONResponse({
        "code": exc.code,
        "message": exc.errmsg,
        "data": exc.data,
    })


# async def http422_error_handler(_: Request, exc: Union[RequestErrorModel])