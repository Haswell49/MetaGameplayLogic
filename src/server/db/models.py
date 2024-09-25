from .base import Model


class Item(Model):
    id: int = 0
    name: str = ""
    price: int = 0
