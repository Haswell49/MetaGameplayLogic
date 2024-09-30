import typing

from .. import base, abstract


class SQLiteAsyncMapper(abstract.AsyncMapper):
    adapter: abstract.AsyncAdapter

    _model_type: typing.Type[base.Model]

    def __init__(self, adapter: abstract.AsyncAdapter, model_type: type[base.Model]):
        self.adapter = adapter
        self._model_type = model_type

    async def create(self, instance: base.Model) -> str | int:
        primary_key = await self.adapter.insert(self._model_type.get_table_name(), instance.data)

        return primary_key

    async def select(self, instance: base.Model) -> base.Model | None:
        values = await self.adapter.select(self._model_type.get_table_name(), **instance.data)

        if not values:
            return None

        data = {key: value for key, value in zip(self._model_type.get_fields(), values)}

        return self._model_type(**data)

    async def update(self, instance: base.Model):
        await self.adapter.update(self._model_type.get_table_name(), instance.data)

    async def delete(self, instance_id: int | str):
        await self.adapter.delete(self._model_type.get_table_name(), instance_id)
