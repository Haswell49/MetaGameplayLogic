from aiohttp import web

from urls import routes

app = web.Application()

app.add_routes(routes)

web.run_app(app, host="127.0.0.1", port=8000)
