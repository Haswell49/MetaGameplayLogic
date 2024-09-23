from src.server.db.formatters import abstract


class Model:
    # TODO: Add SQL type validation
    _table_name: str = ""

    _DEFAULT_SENTINEL_TYPE = None

    @property
    def table_name(self) -> str:
        return self._table_name

    def __init__(self, **kwargs):
        if not self._table_name:
            self._table_name = self._generate_table_name()

        self._setup_data_fields(kwargs)

    async def save(self):
        pass

    def _generate_table_name(self):
        return type(self).__name__.lower() + 's'

    def _setup_data_fields(self, data: dict):
        for field_name in type(self).__dict__.keys():
            if self._filter_field(field_name):
                continue

            value = self._DEFAULT_SENTINEL_TYPE

            if field_name in data:
                value = data[field_name]

            setattr(self, field_name, value)

    def _filter_field(self, field_name: str):
        if field_name.startswith('_'):
            return False
        elif field_name.isupper():
            return False

        return True
