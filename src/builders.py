import abc


class ABCVehicleBuilder(abc.ABC):
    '''
    Specifies methods for creating a builder
    '''

    @abc.abstractproperty
    def vehicle(self) -> None:
        pass

    @abc.abstractmethod
    def make_first_stage(self) -> None:
        pass

    @abc.abstractmethod
    def make_second_stage(self) -> None:
        pass
