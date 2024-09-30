from aiohttp import web
from aiohttp_session import get_session

import crypt
import db
from auth import login, register, UserAlreadyExists


class RegisterView(web.View):
    async def post(self):
        data = await self.request.json()

        data["password"] = crypt.encrypt(data["password"])

        user = db.models.User(**data)

        try:
            user = await register(self.request.app.db_mappers[db.models.User], user)
        except UserAlreadyExists:
            return web.HTTPConflict(f"User '{user}' already exists.")

        session = await get_session(self.request)
        session["user_id"] = user.id

        return web.HTTPOk()


class LoginView(web.View):
    async def post(self):
        data = await self.request.json()

        data["password"] = crypt.encrypt(data["password"])

        user = await login(self.request.app.db_mappers[db.models.User],
                           db.models.User(**data))

        if not user:
            del data["password"]
            return web.HTTPForbidden(body=f"No user with credentials: {data}")

        session = await get_session(self.request)
        session["user_id"] = user.id

        return web.HTTPOk()


