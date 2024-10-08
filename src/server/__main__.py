import asyncio

import aiohttp_session
from aiohttp import web
from aiohttp_session.cookie_storage import EncryptedCookieStorage

import config
import db.models
from apps import SQLApplication
from db.adapters import create_sql_adapter
from db.mappers import create_mappers
from middlewares import auth_middleware
from urls import routes


def init_app(host: str, port: int, web_app: web.Application, event_loop: asyncio.AbstractEventLoop = None):
    web.run_app(web_app, host=host, port=port, loop=event_loop)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()

    sql_adapter = loop.run_until_complete(create_sql_adapter(config.SQL_FORMATTER_TYPE,
                                                             config.SQL_ADAPTER_TYPE,
                                                             config.DB_CONFIG))

    sql_mappers = create_mappers(sql_adapter, config.SQL_MAPPER_TYPE, db.models)

    app = SQLApplication(sql_adapter, sql_mappers)

    aiohttp_session.setup(app, EncryptedCookieStorage(config.COOKIES_SECRET_KEY))

    app.middlewares.append(auth_middleware)

    app.add_routes(routes)

    init_app(config.SERVER_HOST, config.SERVER_PORT, app, event_loop=loop)
