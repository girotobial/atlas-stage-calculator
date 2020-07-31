import abc
import src.parts


class ABCBuilder(abc.ABC):
    '''
    Specifies methods for creating a builder
    '''

    @abc.abstractmethod
    def reset(self) -> None:
        pass

    @abc.abstractproperty
    def product(self) -> None:
        pass


class StageBuilder(ABCBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._stage = src.parts.Stage()

    @property
    def product(self) -> src.parts.Stage:
        product = self._stage
        self.reset()
        return product

    def build(self, product: str):
        '''
        Constructs stage from name of stage

        Parameters
        ----------
        product: str
            Name of the stage
        '''
        # TODO


class VehicleBuilder(ABCBuilder):
    def __init__(self) -> None:
        self._stage_builder = StageBuilder()
        self.reset()

    def reset(self):
        self._vehicle = src.parts.Vehicle()

    @property
    def product(self) -> src.parts.Vehicle:
        product = self._vehicle
        self.reset()
        return product

    def build(self) -> None:
        '''
        Constructs stage from name of stage

        Parameters
        ----------
        product: str
            Name of the stage
        '''
        # TODO
