import db


async def sign_in():
    pass


async def login(db_mapper: db.abstract.Mapper, user: db.models.User) -> db.models.User | None:
    try:
        user = await db_mapper.select(user)
    except db.models.User.DoesNotExist:
        return None

    return user
