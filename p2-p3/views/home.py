from fastapi import Request

async def home(request: Request, id: str):
#                  app是已经被创建的实例
#views的TemplateResponse方法是由application.state.views = Jinja2Templates(directory=settings.TEMPLATE_DIR)创建的
    return request.app.state.views.TemplateResponse("index.html", {"request": request, "id": id})
#request请求访问全局共享的app.state，也能访问request独有的数据
# request.method      # GET/POST
# request.url         # 完整URL
# request.headers     # 请求头
# request.cookies     # Cookie
# request.client      # 客户端IP和端口
# request.query_params # ?name=xxx
# request.path_params # /user/{id} 中的 id