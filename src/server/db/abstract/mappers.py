import abc
from .models import Model
from .adapters import AsyncAdapter


class AsyncMapper(abc.ABC):
    @abc.abstractmethod
    def __init__(self, adapter: AsyncAdapter, model_type: type[Model]):
        pass

    @abc.abstractmethod
    async def create(self, instance: Model) -> str | int:
        pass

    @abc.abstractmethod
    async def select(self, instance: Model) -> Model | None:
        pass

    @abc.abstractmethod
    async def update(self, instance: Model):
        pass

    @abc.abstractmethod
    async def delete(self, instance_id: int | str):
        pass
