import typing

from .. import base, abstract
from .. import adapters


class SQLiteAsyncMapper(abstract.Mapper):
    adapter: abstract.Adapter

    _model_type: typing.Type[base.Model]

    def __init__(self, adapter: abstract.Adapter, model_type: type[base.Model]):
        self.adapter = adapter
        self._model_type = model_type

    async def create(self, instance: base.Model):
        await self.adapter.insert(self._model_type.get_table_name(), instance.data)

    async def select(self, instance: base.Model):
        try:
            values = await self.adapter.select(self._model_type.get_table_name(), **instance.data)
        except adapters.RowNotFoundException:
            raise self._model_type.DoesNotExist

        data = {key: value for key, value in zip(self._model_type.get_fields(), values)}

        return self._model_type(**data)

    async def update(self, instance: base.Model):
        await self.adapter.update(self._model_type.get_table_name(), instance.data)

    async def delete(self, instance_id: int | str):
        await self.adapter.delete(self._model_type.get_table_name(), instance_id)
