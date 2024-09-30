from aiohttp import web
from aiohttp_session import get_session

import crypt
import db
from auth import login, register


class RegisterView(web.View):
    async def post(self):
        data = await self.request.json()

        data["password"] = crypt.encrypt(data["password"])

        user = db.models.User(**data)

        try:
            user_id = await register(self.request.app.db_mappers[db.models.User], user)
        except db.models.User.AlreadyExists:
            return web.HTTPConflict(body=f"User '{user}' already exists.")

        session = await get_session(self.request)
        session["user_id"] = user_id

        return web.HTTPOk()


class LoginView(web.View):
    async def post(self):
        data = await self.request.json()

        data["password"] = crypt.encrypt(data["password"])

        user = db.models.User(**data)

        try:
            user_id = await login(self.request.app.db_mappers[db.models.User],
                                  user)
        except db.models.User.DoesNotExist:
            return web.HTTPForbidden(body=f"User not found: {user}")

        session = await get_session(self.request)
        session["user_id"] = user_id

        return web.HTTPOk()
