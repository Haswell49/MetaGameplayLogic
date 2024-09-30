import db



async def register(db_mapper: db.abstract.Mapper, user: db.models.User):
    user = await db_mapper.select(user)

    if user:
        raise db.models.User.AlreadyExists(f"User: {user.data} already exists")

    await db_mapper.create(user)


async def login(db_mapper: db.abstract.Mapper, user: db.models.User) -> db.models.User | None:
    user = await db_mapper.select(user)

    return user
