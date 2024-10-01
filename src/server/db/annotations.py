class PrimaryKeyType(type):
    def __getitem__(cls, item: type[str | int]):
        return cls(item)


class PrimaryKey(metaclass=PrimaryKeyType):
    def __init__(self, key_type: type[str | int]):
        self.key_type = key_type

    def __call__(self):
        return None

    def __repr__(self):
        return f"{type(self).__name__}({self.key_type})"
