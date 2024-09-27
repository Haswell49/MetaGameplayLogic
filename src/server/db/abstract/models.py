import abc


class Model(abc.ABC):
    @abc.abstractmethod
    async def save(self):
        pass
