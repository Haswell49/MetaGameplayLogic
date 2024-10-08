import dto
import db


async def register(db_mapper: db.abstract.AsyncMapper, user_dto: dto.models.User) -> db.abstract.Model:
    data = user_dto.model_dump(exclude={"password", })

    _user = await db_mapper.select(**data)

    if _user:
        raise db.models.User.AlreadyExists(f"User: {user_dto.email} already exists")

    data["password"] = user_dto.password

    return await db_mapper.create(**data)


async def login(db_mapper: db.abstract.AsyncMapper, user_dto: dto.models.User) -> db.abstract.Model:
    data = user_dto.model_dump()

    user = await db_mapper.select(**data)

    if not user:
        raise db.models.User.DoesNotExist(f"User {user} does not exist or you have entered wrong credentials")

    return user
