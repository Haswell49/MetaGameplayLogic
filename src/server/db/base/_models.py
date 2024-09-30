import typing

from .. import abstract


class Model(abstract.Model):
    # TODO: Add SQL type validation

    _table_name: str = ""

    _data: dict[str, typing.Any]

    class AlreadyExists(Exception):
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

    def __init__(self, **kwargs):
        self._data = dict()

        self._setup_fields(kwargs if kwargs else {})

    async def save(self):
        pass

    def _setup_fields(self, data: dict):
        for field_name, field_type in type(self).__annotations__.items():
            if not self._is_data_field(field_name):
                continue

            value = data.get(field_name, field_type())

            if type(value) is not field_type:
                raise TypeError(f"Invalid type: '{type(value)}' for field '{field_name}' (type: ({field_type})")

            self._data[field_name] = value
            setattr(self, field_name, value)

    def __eq__(self, other):
        if not isinstance(other, Model):
            return False

        return self._data == other._data

    # TODO: Make a standard __repr__ realization for models
