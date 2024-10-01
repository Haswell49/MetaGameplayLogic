import typing

from .. import abstract


# TODO: Add an base class for this class
class SQLiteFormatter(abstract.SQLFormatter):
    def insert(self, table_name: str, data: dict):
        str_columns = ", ".join(data.keys())
        str_values = ", ".join(self._format_query_values(data.values()))

        return f"INSERT INTO {table_name} ({str_columns}) VALUES ({str_values});"

    def select(self, table_name: str, data: dict):
        str_filters = " AND ".join(self._format_equations(data.items()))

        return f"SELECT * FROM {table_name} WHERE {str_filters};"

    def update(self, table_name: str, data: dict):
        row_id = data["id"]

        str_assignments = ", ".join(self._format_equations(data.items()))

        return f"UPDATE {table_name} SET {str_assignments} WHERE id = {row_id};"

    def delete(self, table_name: str, item_id: typing.Any):
        item_id = self._format_value(item_id)

        return f"DELETE FROM {table_name} WHERE id={item_id};"

    def create_table(self, table_name: str, schema: dict):
        formatted_schema = ",".join(f"{key} {value}" for key, value in schema.items())

        return f"CREATE TABLE {table_name} ({formatted_schema});)"

    def _format_query_values(self, values: typing.Iterable):
        for value in values:
            yield self._format_value(value)

    def _format_equations(self, items: typing.ItemsView[str, typing.Any]):
        for key, value in items:
            value = self._format_value(value)
            yield f"{key}={value}"

    def _format_value(self, value: typing.Any):
        if value is None:
            return "NULL"

        if isinstance(value, str):
            return f"'{value}'"

        return f"{value}"
