import types

from .. import abstract
from .. import base


def create_mappers(adapter: abstract.Adapter,
                   mapper_type: type[abstract.Mapper],
                   models: types.ModuleType):
    for model_name in vars(models):
        model_type = getattr(models, model_name)

        if not issubclass(model_type, base.Model):
            continue

        yield mapper_type(adapter, model_type)
