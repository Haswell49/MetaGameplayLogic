import abc
from .models import Model
from .adapters import AsyncAdapter


class AsyncMapper(abc.ABC):
    @abc.abstractmethod
    def __init__(self, adapter: AsyncAdapter, model_type: type[Model]):
        pass

    @abc.abstractmethod
    async def create(self, **data) -> Model:
        pass

    @abc.abstractmethod
    async def select(self, **data) -> Model | None:
        pass

    @abc.abstractmethod
    async def update(self, instance: Model):
        pass

    @abc.abstractmethod
    async def delete(self, instance: Model):
        pass
