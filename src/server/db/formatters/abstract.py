import abc
import typing


class SQLFormatter(abc.ABC):
    @abc.abstractmethod
    def insert(self, table_name: str, data: dict):
        pass

    @abc.abstractmethod
    def select(self, table_name: str, item_id: typing.Any):
        pass

    @abc.abstractmethod
    def update(self, table_name: str, data: dict):
        pass

    @abc.abstractmethod
    def delete(self, table_name: str, item_id: typing.Any):
        pass

    @abc.abstractmethod
    def create_table(self, table_name: str, schema: dict):
        pass
