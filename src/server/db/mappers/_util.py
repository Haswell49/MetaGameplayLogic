import types
from inspect import isclass

from .. import abstract
from .. import base


def create_mappers(adapter: abstract.AsyncAdapter,
                   mapper_type: type[abstract.AsyncMapper],
                   models: types.ModuleType) -> dict[type[abstract.Model], abstract.AsyncMapper]:
    result = dict()

    for model_name in vars(models):
        model_type = getattr(models, model_name)

        if not isclass(model_type):
            continue

        if not issubclass(model_type, base.Model):
            continue

        if model_type is base.Model:
            continue

        result[model_type] = mapper_type(adapter, model_type)

    return result
