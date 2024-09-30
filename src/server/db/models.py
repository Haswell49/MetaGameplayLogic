from .base import Model


class User(Model):
    id: int
    email: str
    password: str

    def __str__(self):
        return f"<{type(self).__name__} '{self.email}'>"


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
