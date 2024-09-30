import abc
import typing

from .formatters import SQLFormatter


class AsyncAdapter(abc.ABC):
    connection: typing.Any

    formatter: SQLFormatter

    @staticmethod
    @abc.abstractmethod
    def create_connection(db_config: dict) -> typing.Any:
        pass

    @abc.abstractmethod
    def __init__(self, connection: typing.Any, formatter: SQLFormatter) -> None:
        pass

    @abc.abstractmethod
    async def insert(self, table_name: str, data: dict) -> int | str:
        pass

    @abc.abstractmethod
    async def select(self, table_name: str, **filters) -> tuple:
        pass

    @abc.abstractmethod
    async def update(self, table_name: str, data: dict) -> None:
        pass

    @abc.abstractmethod
    async def delete(self, table_name: str, item_id: typing.Any) -> None:
        pass
