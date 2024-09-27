import abc
import typing



class Adapter(abc.ABC):
    @abc.abstractmethod
    def insert(self, table_name: str, data: dict) -> None:
        pass

    @abc.abstractmethod
    def select(self, table_name: str, item_id: typing.Any) -> tuple:
        pass

    @abc.abstractmethod
    def update(self, table_name: str, data: dict) -> None:
        pass

    @abc.abstractmethod
    def delete(self, table_name: str, item_id: typing.Any) -> None:
        pass
