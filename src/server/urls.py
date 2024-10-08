from aiohttp import web

from views import PlayerView
from views import RegisterView, LoginView

routes = [
    web.view("/auth/login/", LoginView),
    web.view("/auth/register/", RegisterView),
    web.view("/player/", PlayerView),
    # web.view("/player/balance", BalanceView)
]
     