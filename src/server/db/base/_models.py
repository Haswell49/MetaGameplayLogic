import typing

from src.server.db.formatters import abstract


class Model:
    # TODO: Add SQL type validation

    _table_name: str = ""

    _data: dict[str, typing.Any]

    @classmethod
    def get_table_name(cls):
        if not cls._table_name:
            cls._table_name = cls._generate_table_name()

        return cls._table_name

    @classmethod
    def get_fields(cls) -> typing.Generator[str, None, None]:
        for field_name in cls.__dict__.keys():
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
        for field_name, value in data.items():
            setattr(self, field_name, value)

    def __setattr__(self, field_name: str, value):
        super().__setattr__(field_name, value)

        if not self._is_data_field(field_name):
            return

        self._data[field_name] = value

    def __eq__(self, other):
        if not isinstance(other, Model):
            return False

        return self._data == other._data
