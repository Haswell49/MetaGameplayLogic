import functools

import pydantic
from aiohttp import web
from aiohttp.web import middleware
from aiohttp_session import get_session

import dto
from views import RegisterView, LoginView


@middleware
async def user_data_validation_middleware(request: web.Request, handler: functools.partial):
    if handler.keywords["handler"] not in (LoginView, RegisterView):
        return await handler(request)

    data = await request.json()

    try:
        dto.models.User.model_validate(data)
    except pydantic.ValidationError as error:
        print(repr(error))
        return web.HTTPBadRequest(body="Request data invalid")

    return await handler(request)


@middleware
async def auth_middleware(request: web.Request, handler: functools.partial):
    if handler.keywords["handler"] in (LoginView, RegisterView):
        return await handler(request)

    session = await get_session(request)

    if not session.get("user_id", None):
        return web.HTTPUnauthorized()

    return await handler(request)
