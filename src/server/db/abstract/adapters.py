import abc
import typing

from .formatters import SQLFormatter


class Adapter(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def create_connection(db_config: dict) -> typing.Any:
        pass

    @abc.abstractmethod
    def __init__(self, connection: typing.Any, formatter: SQLFormatter) -> None:
        pass

    @abc.abstractmethod
    def insert(self, table_name: str, data: dict) -> None:
        pass

    @abc.abstractmethod
    def select(self, table_name: str, **filters) -> tuple:
        pass

    @abc.abstractmethod
    def update(self, table_name: str, data: dict) -> None:
        pass

    @abc.abstractmethod
    def delete(self, table_name: str, item_id: typing.Any) -> None:
        pass
