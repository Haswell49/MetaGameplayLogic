import functools

from aiohttp import web
from aiohttp.web import middleware
from aiohttp_session import get_session

from views import RegisterView, LoginView


@middleware
async def auth_middleware(request: web.Request, handler: functools.partial):
    if handler in (LoginView, RegisterView):
        return await handler(request)

    session = await get_session(request)

    if not session.get("user_id", None):
        return web.HTTPUnauthorized()

    return await handler(request)
