import pydantic


class User(pydantic.BaseModel):
    id: int
    email: pydantic.EmailStr
    password: str


class Item(pydantic.BaseModel):
    id: int
    name: str
    price: int
    owner_id: int | None


class Player(pydantic.BaseModel):
    user_id: int
    nickname: str
    items: list[Item]
