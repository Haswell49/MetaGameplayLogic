import pydantic
from . import base


class User(base.BaseUser):
    id: int | None = None


class Item(pydantic.BaseModel):
    id: int | None = None
    name: str
    price: int
    owner_id: int | None = None


class Player(pydantic.BaseModel):
    id: int | None = None
    nickname: str
    items: list[Item] = []
    balance: int = 0
