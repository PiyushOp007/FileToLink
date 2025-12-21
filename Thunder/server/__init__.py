# Thunder/server/__init__.py

from aiohttp import web
from .stream_routes import routes


@web.middleware
async def request_logger_middleware(request, handler):
    print(f"DEBUG: Incoming Request: {request.method} {request.path}")
    return await handler(request)

async def web_server():
    web_app = web.Application(client_max_size=30000000, middlewares=[request_logger_middleware])
    web_app.add_routes(routes)
    return web_app
