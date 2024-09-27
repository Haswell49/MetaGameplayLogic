import abc
from .models import Model
from .adapters import Adapter


class Mapper(abc.ABC):
    @abc.abstractmethod
    def __init__(self, adapter: Adapter, model_type: type[Model]):
        pass

    @abc.abstractmethod
    def create(self, model_instance: Model):
        pass

    @abc.abstractmethod
    def select(self, instance_id: int | str):
        pass

    @abc.abstractmethod
    def update(self, model_instance: Model):
        pass

    @abc.abstractmethod
    def delete(self, instance_id: int | str):
        pass
