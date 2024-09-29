import pydantic
from aiohttp import web

from auth import login
import dto
import db


class LoginView(web.View):
    async def post(self):
        data = await self.request.json()

        try:
            dto.models.User.model_validate(data)
        except pydantic.ValidationError as error:
            print(repr(error))
            return web.HTTPBadRequest(body="Login data invalid")

        user = await login(self.request.app.db_mappers[db.models.User],
                           db.models.User(**data))

        if not user:
            return web.HTTPForbidden(body=f"No user with credentials: {data}")

        return web.HTTPOk()
