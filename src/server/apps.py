from aiohttp import web

import db


class SQLApplication(web.Application):
    def __init__(self, db_adapter: db.abstract.Adapter,
                 db_mappers: dict[type[db.abstract.Model], db.abstract.Mapper],
                 *args,
                 **kwargs):
        super().__init__(*args, **kwargs)

        self.db_adapter = db_adapter
        self.db_mappers = db_mappers
