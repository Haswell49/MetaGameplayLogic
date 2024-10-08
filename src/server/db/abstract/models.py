import abc
import typing


class Model(abc.ABC):
    id: typing.Any

    @property
    @abc.abstractmethod
    def data(self) -> dict[str, typing.Any]:
        pass
