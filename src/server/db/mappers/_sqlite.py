import typing

from .. import base, abstract
from ..adapters import SQLiteAsyncAdapter


class SQLiteAsyncMapper(abstract.AsyncMapper):
    adapter: SQLiteAsyncAdapter

    _model_type: typing.Type[base.Model]

    def __init__(self, adapter: SQLiteAsyncAdapter, model_type: type[base.Model]):
        self.adapter = adapter
        self._model_type = model_type

    async def create(self, **data) -> base.Model:
        primary_key = await self.adapter.insert(self._model_type.get_table_name(), data)

        instance = self._model_type(bound=True, **data)

        if instance.id is None:
            instance.id = primary_key

        return instance

    async def select(self, **data) -> base.Model | None:
        values = await self.adapter.select(self._model_type.get_table_name(), data)

        if not values:
            return None

        data = {key: value for key, value in zip(self._model_type.get_fields(), values)}

        return self._model_type(bound=True, **data)

    async def update(self, instance: base.Model):
        await self.adapter.update(self._model_type.get_table_name(), instance.data)

    async def delete(self, instance: base.Model):
        if not instance.bound:
            raise ValueError("Can't delete an unbound model")

        await self.adapter.delete(self._model_type.get_table_name(), instance.id)

        instance.id = None
