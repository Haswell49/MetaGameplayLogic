import abc
import typing


class Model(abc.ABC):
    @property
    @abc.abstractmethod
    def data(self) -> dict[str, typing.Any]:
        pass
