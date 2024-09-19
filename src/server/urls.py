from aiohttp import web

from src.server.views import LoginView

routes = [
    web.get("/", LoginView.get),
]
