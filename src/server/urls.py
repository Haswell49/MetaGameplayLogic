from aiohttp import web

from views import RegisterView, LoginView

routes = [
    web.view("/auth/login/", LoginView),
    web.view("/auth/register/", RegisterView)
]
