from aiohttp import web


class LoginView(web.View):
    async def get(self):
        return web.Response(text="Hello World")
