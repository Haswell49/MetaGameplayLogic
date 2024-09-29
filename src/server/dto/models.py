import pydantic
from . import base


class User(base.BaseUser):
    id: int | None = None


class Item(pydantic.BaseModel):
    id: int
    name: str
    price: int
    owner_id: int | None = None


class Player(pydantic.BaseModel):
    user_id: int
    nickname: str
    items: list[Item]
