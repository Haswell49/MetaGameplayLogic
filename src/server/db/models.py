from .base import Model


class User(Model):
    id: int
    email: str
    password: str

    def __str__(self):
        return f"<{self.__class__.__name__} '{self.email}' ({None or self.id})>"


class Item(Model):
    id: int
    name: str
    price: int
    owner_id: int

    def __str__(self):
        return f"<{self.__class__.__name__} '{self.name}' (id={None or self.id}, owner_id={None or self.owner_id})>"


class Player(Model):
    id: int
    nickname: str
    balance: int

    def __str__(self):
        return f"<{type(self).__name__} '{self.nickname}' ({'' or self.id}>"
