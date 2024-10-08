from aiohttp import web
from aiohttp_session import get_session

import crypt
import db
import dto
from auth import login, register
from game import create_player


class BaseDBView(web.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.mapper = self.request.app.db_mappers[self._model]


class RegisterView(BaseDBView):
    _model = db.models.User

    async def post(self):
        data = await self.request.json()

        data["password"] = crypt.encrypt(data["password"])

        user_dto = dto.models.User(**data)

        try:
            user = await register(self.mapper, user_dto)
        except self._model.AlreadyExists:
            return web.HTTPConflict(body=f"User '{user_dto.email}' already exists.")

        session = await get_session(self.request)
        session["user_id"] = user.id

        return web.HTTPOk()


class LoginView(BaseDBView):
    _model = db.models.User

    async def post(self):
        data = await self.request.json()

        data["password"] = crypt.encrypt(data["password"])

        user_dto = dto.models.User(**data)

        try:
            user = await login(self.mapper, user_dto)
        except db.models.User.DoesNotExist:
            return web.HTTPForbidden(body=f"User not found: {user_dto.email}")

        session = await get_session(self.request)
        session["user_id"] = user.id

        return web.HTTPOk()


class PlayerView(BaseDBView):
    _model = db.models.Player

    mapper: db.abstract.AsyncMapper

    async def get(self):
        session = await get_session(self.request)

        player = await self.mapper.select(id=session["user_id"])

        if not player:
            return web.HTTPNotFound()

        return web.json_response(player.data)

    async def post(self):
        data = await self.request.json()

        session = await get_session(self.request)

        player_dto = dto.models.Player(id=session["user_id"], **data)

        try:
            await create_player(self.mapper, player_dto)
        except db.models.Player.AlreadyExists:
            return web.HTTPConflict(body=f"Player for user (id={player_dto.id}) already exists.")

        return web.HTTPOk()
