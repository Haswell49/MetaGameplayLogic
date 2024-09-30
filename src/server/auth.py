import db


async def register(db_mapper: db.abstract.AsyncMapper, user: db.models.User) -> str | int:
    _user = await db_mapper.select(user)

    if _user:
        raise db.models.User.AlreadyExists(f"User: {user} already exists")

    return await db_mapper.create(user)


async def login(db_mapper: db.abstract.AsyncMapper, user: db.models.User) -> str | int:
    user = await db_mapper.select(user)

    if not user:
        raise db.models.User.DoesNotExist(f"User {user} does not exist")

    return user.id
