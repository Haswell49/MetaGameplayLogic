from aiohttp import web

from views import LoginView

routes = [
    web.view("/login/", LoginView)
]
