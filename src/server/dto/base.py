import pydantic


class BaseUser(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: str
