import db
import dto


async def create_player(player_mapper: db.abstract.AsyncMapper, player_dto: dto.models.Player) -> db.abstract.Model:
    data = player_dto.model_dump(exclude={"items"})

    player = await player_mapper.select(id=player_dto.id)

    if player:
        raise db.models.Player.AlreadyExists

    return await player_mapper.create(**data)
