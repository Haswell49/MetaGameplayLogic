from aiohttp import web

from .views import LoginView

routes = [
    web.get("/", LoginView.get),
]
