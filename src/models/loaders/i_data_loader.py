import abc
import typing

class IDataLoader(abc.ABC):

    @abc.abstractclassmethod
    def load_data() -> typing.Dict:
        pass