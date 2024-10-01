import typing

from .. import abstract


class Model(abstract.Model):
    # TODO: Add SQL type validation

    PRIMARY_KEY_FIELD = "id"

    _table_name: str = ""

    _data: dict[str, typing.Any]

    _bound: bool

    class AlreadyExists(Exception):
        pass

    class DoesNotExist(Exception):
        pass

    # TODO: Solve this mess of static methods (might need to create a separate instance type for this)
    @classmethod
    def get_table_name(cls):
        if not cls._table_name:
            cls._table_name = cls._generate_table_name()

        return cls._table_name

    @classmethod
    def get_fields(cls) -> typing.Generator[str, None, None]:
        for field_name in cls.__annotations__.keys():
            if not cls._is_data_field(field_name):
                continue

            yield field_name

    @classmethod
    def _generate_table_name(cls):
        return cls.__name__.lower() + 's'

    @staticmethod
    def _is_data_field(field_name: str):
        if field_name.startswith('_'):
            return False
        elif field_name.isupper():
            return False

        return True

    @property
    def data(self) -> dict[str, typing.Any]:
        return self._data

    @property
    def bound(self) -> bool:
        return self._bound

    def __init__(self, bound=False, **kwargs):
        self._data = dict()

        self._bound = bound

        self._setup_fields(kwargs)

    async def save(self):
        pass

    def _setup_fields(self, data: dict):
        for field_name, field_type in type(self).__annotations__.items():
            value = data.get(field_name, None)
            self.__setattr__(field_name, value)

    def __setattr__(self, key: str, value: typing.Any):
        super().__setattr__(key, value)

        if self._is_data_field(key):
            self._data[key] = value

    def __eq__(self, other):
        if not isinstance(other, Model):
            return False

        return self._data == other._data

    # TODO: Make a standard __repr__ realization for models
