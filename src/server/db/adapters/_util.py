from .. import abstract


async def create_sql_adapter(formatter_type: type[abstract.SQLFormatter],
                             adapter_type: type[abstract.Adapter],
                             db_config: dict):
    sql_formatter = formatter_type()

    connection = await adapter_type.create_connection(db_config)

    adapter = adapter_type(connection, sql_formatter)

    return adapter
