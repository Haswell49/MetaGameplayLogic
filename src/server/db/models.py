from .base import Model


class User(Model):
    id: int
    email: str
    password: str


class Item(Model):
    id: int
    name: str
    price: int
    owner_id: int


class Player(Model):
    user_id: int
    nickname: str
    items: list[Item]
    balance: int
