import typing
from collections.abc import Iterable

from .. import abstract


# TODO: Add an base class for this class
class SQLiteFormatter(abstract.SQLFormatter):
    def insert(self, table_name: str, data: dict):
        columns = self._sanitize_columns(data.items())
        values = self._sanitize_values(data.values())

        str_columns = ", ".join(columns)
        str_values = ", ".join(values)

        return f"INSERT INTO {table_name} ({str_columns}) VALUES ({str_values});"

    def select(self, table_name: str, data: dict):
        columns = self._sanitize_columns(data.items())
        values = self._sanitize_values(data.values())

        str_filters = " AND ".join(self._format_items(columns, values, '='))

        return f"SELECT * FROM {table_name} WHERE {str_filters};"

    def update(self, table_name: str, data: dict):
        row_id = data["id"]

        columns = self._sanitize_columns(data.items())
        values = self._sanitize_values(data.values())

        str_assignments = ", ".join(self._format_items(columns, values, "="))

        return f"UPDATE {table_name} SET {str_assignments} WHERE id = {row_id};"

    def delete(self, table_name: str, item_id: typing.Any):
        item_id = self._sanitize(item_id)

        return f"DELETE FROM {table_name} WHERE id={item_id};"

    def create_table(self, table_name: str, schema: dict):
        formatted_schema = ",".join(f"{key} {value}" for key, value in schema.items())

        return f"CREATE TABLE {table_name} ({formatted_schema});)"

    def _sanitize_columns(self, items: typing.ItemsView[str, typing.Any]):
        for key, value in items:
            if value is None:
                continue

            yield key

    def _sanitize_values(self, values: Iterable):
        for value in values:
            if value is None:
                continue

            value = self._sanitize(value)

            yield value

    def _format_items(self,
                      columns: typing.Iterable[str],
                      values: typing.Iterable[typing.Any],
                      separator: str):
        for key, value in zip(columns, values):
            yield f"{key}{separator}{value}"

    def _sanitize(self, value: typing.Any):
        if isinstance(value, str):
            return f"'{value}'"

        return f"{value}"
