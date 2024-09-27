import typing

from ..adapters import SQLiteAsyncAdapter
from .. import base, abstract


class SQLiteAsyncMapper(abstract.Mapper):
    adapter: abstract.Adapter

    _model_type: typing.Type[base.Model]

    def __init__(self, adapter: abstract.Adapter, model_type: typing.Type[base.Model]):
        self.adapter = adapter
        self._model_type = model_type

    async def create(self, model_instance: base.Model):
        await self.adapter.insert(self._model_type.get_table_name(), model_instance.data)

    async def select(self, instance_id: int | str):
        values = await self.adapter.select(self._model_type.get_table_name(), instance_id)

        data = {key: value for key, value in zip(self._model_type.get_fields(), values)}

        return self._model_type(**data)

    async def update(self, model_instance: base.Model):
        await self.adapter.update(self._model_type.get_table_name(), model_instance.data)

    async def delete(self, instance_id: int | str):
        await self.adapter.delete(self._model_type.get_table_name(), instance_id)
