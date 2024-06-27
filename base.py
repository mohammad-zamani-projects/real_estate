from abc import ABC


class BaseClass(ABC):
    object_list = list()
    _id = 0

    def __init__(self, *args, **kwargs):
        self.store_objects(self)
        self.id = self.id_adder()
        super.__init__(*args, **kwargs)

    @classmethod
    def store_objects(cls, obj):
        cls.object_list.append(obj)

    @classmethod
    def id_adder(cls):
        cls._id += 1
        return cls._id


