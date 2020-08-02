from __future__ import annotations
import abc
from typing import List
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

    _STAGE_DICT = {
        'Able': {
            "Engines": ["Vanguard-12 Able"],
            "Tanks": ["Vanguard-100"],
            "Couplers": ["Vanguard-4688 Fairing"]
        },
        'Atlas BT': {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Tapered"],
            "Couplers": []
        },
        'Atlas BMT': {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Medium", "Atlas-Tapered"],
            "Couplers": []
        },
        'Atlas ICBM Skirt': {
            "Engines": [
                "LR89-5 90%",
                "LR89-5 90%",
                "LR105-nm",
                "LR101-nm",
                "LR101-nm"
            ],
            "Tanks": [],
            "Couplers": ["Atlas-BoosterSkirt"]
        },
        "Atlas LR89-5 Skirt": {
            "Engines": [
                "LR89-5",
                "LR89-5",
                "LR105-nm",
                "LR101-nm",
                "LR101-nm"
            ],
            "Tanks": [],
            "Couplers": ["Atlas-BoosterSkirt"]
        }
    }

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._stage = src.parts.Stage()

    @property
    def product(self) -> src.parts.Stage:
        product = self._stage
        self.reset()
        return product

    def _add_tanks(self, tank_list: List[str]) -> None:
        for tank in tank_list:
            if tank is not None:
                self._stage.add(src.parts.Tank(tank))

    def _add_engines(self, engine_list: List[str]) -> None:
        for engine in engine_list:
            if engine is not None:
                self._stage.add(src.parts.Engine(engine))

    def _add_couplers(self, coupler_list: List[str]) -> None:
        # re-activate once written Coupler class in parts
        # for coupler in coupler_list:
        #    self._stage.add(src.parts.Coupler(coupler))
        pass

    def build_standard(self, stage_name: str) -> StageBuilder:
        '''
        Constructs stage from name of stage

        Parameters
        ----------
        product: str
            Name of the stage
        '''
        if stage_name not in self._STAGE_DICT.keys():
            raise ValueError(f'{stage_name} is not a standard stage')

        vehicle_details = self._STAGE_DICT.get(stage_name)
        self._add_engines(vehicle_details['Engines'])
        self._add_tanks(vehicle_details['Tanks'])
        self._add_couplers(vehicle_details['Couplers'])
        return self


class VehicleBuilder(ABCBuilder):

    _VEHICLE_DICT = {
        "Atlas-B": [
            "Atlas ICBM Skirt",
            "Atlas BT"
        ],
        "Atlas-D": [
            "Atlas ICBM Skirt",
            "Atlas BMT"
        ],
        "Atlas-D Able": [
            "Atlas ICBM Skirt",
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

    def reset(self) -> None:
        self._vehicle = src.parts.Vehicle()

    @property
    def product(self) -> src.parts.Vehicle:
        product = self._vehicle
        self.reset()
        return product

    def build_standard(self, vehicle) -> VehicleBuilder:
        '''
        Constructs stage from name of stage

        Parameters
        ----------
        product: str
            Name of the stage
        '''
        if vehicle not in self._VEHICLE_DICT:
            raise ValueError(f'{vehicle} is not a standard vehicle')

        for s in self._VEHICLE_DICT.get(vehicle):
            self._stage_builder.build_standard(s)
            self._vehicle.add(self._stage_builder.product)
        return self

    def name(self, name) -> VehicleBuilder:
        self._vehicle.name = name
        return self    

    def add_payload(self, payload_mass) -> VehicleBuilder:
        self._vehicle.payload_mass = payload_mass
        return self
