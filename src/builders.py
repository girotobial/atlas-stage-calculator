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

    VEHICLE_DICT = {
        "Atlas-B": [
            "Atlas ICMB Skirt",
            "Atlas BT"
        ],
        "Atlas-D": [
            "Atlas ICMB Skirt",
            "Atlas BMT"
        ],
        "Atlas-D Able": [
            "Atlas ICMB Skirt",
            "Atlas BMT",
            "Able"
        ],
        "Atlas LV-3A": [
            "Atlas LR89-5 Skirt",
            "Atlas BMT"
        ],
        "Atlas LV-3A Agena-A": [
            "Atlas LR89-5 Skirt",
            "Atlas BMT",
            "Agena-A"
        ],
        "Atlas LV-3A Agena-B": [
            "Atlas LR89-5 Skirt",
            "Atlas BMT",
            "Agena-B"
        ],
        "Atlas LV-3A Agena-D": [
            "Atlas LR89-5 Skirt",
            "Atlas BMT",
            "Agena-D"
        ],
        "Atlas LV-3C": [
            "Atlas LR89-5 Skirt",
            "Atlas BMM",
        ],
        "Atlas SLV-3": [
            "Atlas LR89-7 Skirt",
            "Atlas BMT",
        ],
        "Atlas SLV-3 Agena-D": [
            "Atlas LR89-7 Skirt",
            "Atlas BMT",
            "Agena-D"
        ],
        "Atlas SLV-3A": [
            "Atlas LR89-7 Skirt",
            "Atlas BMST"
        ],
        "Atlas SLV-3A Agena-D": [
            "Atlas LR89-7 Skirt",
            "Atlas BMST",
            "Agena-D"
        ],
        "Atlas SLV-3B": [
            "Atlas LR89-7 Skirt",
            "Atlas BMM",
        ],
        "Atlas SLV-3B Agena-D": [
            "Atlas LR89-7 Skirt",
            "Atlas BMM",
            "Agena-D"
        ],
        "Atlas SLV-3C": [
            "Atlas LR89-7 Skirt",
            "Atlas BMM",
            "Centaur-D"
        ],
        "Atlas SLV-3D": [
            "Atlas LR89-7 Skirt",
            "Atlas BMM",
            "Centaur-D1A"
        ],
        "Atlas E/F": [
            "Atlas LR89-7 Skirt",
            "Atlas BM",
            "Staara-37/48B"
        ],
        "Atlas H": [
            "Atlas LR89-7 Skirt",
            "Atlas BMM",
        ],
        "Atlas I": [
            "Atlas LR89-7 Skirt",
            "Atlas BMMS",
            "Centaur-D1A"
        ],
        "Atlas II": [
            "Atlas RS56 Skirt",
            "Atlas BMMM",
            "Centaur-II"
        ],
        "Atlas II Centaur-II": [
            "Atlas RS56 Skirt",
            "Atlas BMMM",
            "Centaur-II"
        ],
        "Atlas IIAS": [
            "4x Dioscuri-4A",
            "Atlas RS56 Skirt",
            "Atlas BMMM",
            "Centaur-II"
        ],
    }

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
