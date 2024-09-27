import abc
from .models import Model


class Mapper(abc.ABC):
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
