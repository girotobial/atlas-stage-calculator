from __future__ import annotations

import abc
from typing import Dict, List, cast

import src.parts


class ABCBuilder(abc.ABC):
    """
    Specifies methods for creating a builder
    """

    @abc.abstractmethod
    def reset(self) -> None:
        pass

    @abc.abstractproperty
    def product(self):
        pass


class StageBuilder(ABCBuilder):

    _STAGE_DICT = {
        "Able": {
            "Engines": ["Vanguard-12 Able"],
            "Tanks": ["Vanguard-100"],
            "Accessories": ["Vanguard-4688 Fairing"],
        },
        "Atlas BT": {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Tapered"],
            "Accessories": [],
        },
        "Atlas BM": {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Medium"],
            "Accessories": [],
        },
        "Atlas BMT": {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Medium", "Atlas-Tapered"],
            "Accessories": [],
        },
        "Atlas BMST": {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Medium", "Atlas-Small", "Atlas-Tapered"],
            "Accessories": [],
        },
        "Atlas BMM": {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Medium", "Atlas-Medium"],
            "Accessories": [],
        },
        "Atlas BMMS": {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Medium", "Atlas-Medium", "Atlas-Small"],
            "Accessories": [],
        },
        "Atlas BMMM": {
            "Engines": ["LR105", "LR101", "LR101"],
            "Tanks": ["Atlas-Base", "Atlas-Medium", "Atlas-Medium", "Atlas-Medium"],
            "Accessories": [],
        },
        "Atlas ICBM Skirt": {
            "Engines": ["LR89-5 90%", "LR89-5 90%", "LR105-nm", "LR101-nm", "LR101-nm"],
            "Tanks": [],
            "Accessories": ["Atlas-BoosterSkirt"],
        },
        "Atlas LR89-5 Skirt": {
            "Engines": ["LR89-5", "LR89-5", "LR105-nm", "LR101-nm", "LR101-nm"],
            "Tanks": [],
            "Accessories": ["Atlas-BoosterSkirt"],
        },
        "Atlas LR89-7 Skirt": {
            "Engines": ["LR89-7", "LR89-7", "LR105-nm", "LR101-nm", "LR101-nm"],
            "Tanks": [],
            "Accessories": ["Atlas-BoosterSkirt"],
        },
        "Atlas RS56 Skirt": {
            "Engines": ["RS56", "RS56", "LR105-nm", "LR101-nm", "LR101-nm"],
            "Tanks": [],
            "Accessories": ["Atlas-BoosterSkirt"],
        },
        "Agena-A": {
            "Engines": ["Agena-A-25"],
            "Tanks": ["Agena-70W"],
            "Accessories": [],
        },
        "Agena-B": {
            "Engines": ["Agena-A-25"],
            "Tanks": ["Agena-200B"],
            "Accessories": [],
        },
        "Agena-D": {
            "Engines": [
                "Agena-D-35",
                "Agena-D-4",
                "Agena-D-4",
            ],
            "Tanks": ["Agena-200D"],
            "Accessories": [],
        },
        "Centaur-D": {
            "Engines": [
                "Centaur-R-10A",
                "Centaur-R-10A",
            ],
            "Tanks": ["Centaur-D-1440"],
            "Accessories": [
                "Centaur ACS",
                "Centaur 1.875m Fairing Base",
                "Centaur Engine Mounting Plate",
            ],
        },
        "Centaur-D1A": {
            "Engines": [
                "Centaur-R-10A-3",
                "Centaur-R-10A-3",
            ],
            "Tanks": ["Centaur-D-1800"],
            "Accessories": [
                "Centaur ACS",
                "Centaur 1.875m Fairing Base",
                "Centaur Engine Mounting Plate",
            ],
        },
        "Centaur-II": {
            "Engines": [
                "Centaur-R-10A-4",
            ],
            "Tanks": ["Centaur-D-2160"],
            "Accessories": [
                "Centaur ACS",
                "Centaur 1.875m Fairing Base",
                "Centaur Engine Mounting Plate",
            ],
        },
        "4x Castor-4A": {
            "Engines": [
                "Castor-4A",
                "Castor-4A",
                "Castor-4A",
                "Castor-4A",
            ],
            "Tanks": [],
            "Accessories": [],
        },
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

    def _add_accessories(self, accessory_list: List[str]) -> None:
        for accessory in accessory_list:
            self._stage.add(src.parts.Accessory(accessory))

    def build_standard(self, stage_name: str) -> StageBuilder:
        """
        Constructs stage from name of stage

        Parameters
        ----------
        product: str
            Name of the stage
        """
        if stage_name not in self._STAGE_DICT.keys():
            raise ValueError(f"{stage_name} is not a standard stage")

        self._stage.name = stage_name

        stage_details = cast(Dict[str, List[str]], self._STAGE_DICT[stage_name])
        self._add_engines(stage_details["Engines"])
        self._add_tanks(stage_details["Tanks"])
        self._add_accessories(stage_details["Accessories"])
        return self


class VehicleBuilder(ABCBuilder):

    _VEHICLE_DICT = {
        "Atlas-B": ["Atlas ICBM Skirt", "Atlas BT"],
        "Atlas-D": ["Atlas ICBM Skirt", "Atlas BMT"],
        "Atlas-D Able": ["Atlas ICBM Skirt", "Atlas BMT", "Able"],
        "Atlas LV-3A": ["Atlas LR89-5 Skirt", "Atlas BMT"],
        "Atlas LV-3A Agena-A": ["Atlas LR89-5 Skirt", "Atlas BMT", "Agena-A"],
        "Atlas LV-3A Agena-B": ["Atlas LR89-5 Skirt", "Atlas BMT", "Agena-B"],
        "Atlas LV-3A Agena-D": ["Atlas LR89-5 Skirt", "Atlas BMT", "Agena-D"],
        "Atlas LV-3C": [
            "Atlas LR89-5 Skirt",
            "Atlas BMM",
        ],
        "Atlas SLV-3": [
            "Atlas LR89-7 Skirt",
            "Atlas BMT",
        ],
        "Atlas SLV-3 Agena-D": ["Atlas LR89-7 Skirt", "Atlas BMT", "Agena-D"],
        "Atlas SLV-3A": ["Atlas LR89-7 Skirt", "Atlas BMST"],
        "Atlas SLV-3A Agena-D": ["Atlas LR89-7 Skirt", "Atlas BMST", "Agena-D"],
        "Atlas SLV-3B": [
            "Atlas LR89-7 Skirt",
            "Atlas BMM",
        ],
        "Atlas SLV-3B Agena-D": ["Atlas LR89-7 Skirt", "Atlas BMM", "Agena-D"],
        "Atlas SLV-3C": ["Atlas LR89-7 Skirt", "Atlas BMM", "Centaur-D"],
        "Atlas SLV-3D": ["Atlas LR89-7 Skirt", "Atlas BMM", "Centaur-D1A"],
        "Atlas E/F": ["Atlas LR89-7 Skirt", "Atlas BM", "Staara-37/48B"],
        "Atlas H": [
            "Atlas LR89-7 Skirt",
            "Atlas BMM",
        ],
        "Atlas I": ["Atlas LR89-7 Skirt", "Atlas BMMS", "Centaur-D1A"],
        "Atlas II": ["Atlas RS56 Skirt", "Atlas BMMM", "Centaur-II"],
        "Atlas II Centaur-II": ["Atlas RS56 Skirt", "Atlas BMMM", "Centaur-II"],
        "Atlas IIAS": ["4x Castor-4A", "Atlas RS56 Skirt", "Atlas BMMM", "Centaur-II"],
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
        """
        Constructs stage from name of stage

        Parameters
        ----------
        product: str
            Name of the stage
        """
        if vehicle not in self._VEHICLE_DICT:
            raise ValueError(f"{vehicle} is not a standard vehicle")

        self._vehicle.name = vehicle

        for s in self._VEHICLE_DICT[vehicle]:
            self._stage_builder.build_standard(s)
            self._vehicle.add(self._stage_builder.product)
        return self

    def name(self, name) -> VehicleBuilder:
        self._vehicle.name = name
        return self

    def add_payload(self, payload_mass) -> VehicleBuilder:
        self._vehicle.payload_mass = payload_mass
        return self
