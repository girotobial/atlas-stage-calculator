'''
Class for decouplers
(bits that seperate the spacecraft into stages)
'''
from __future__ import annotations
import json
from typing import List
from src.parts.abc_parts import ABCPart
from src.constants import CONFIG_PATH


class Coupler(ABCPart):
    def __init__(self, name: str = 'Custom') -> None:
        self._name = name
        if name == 'Custom':
            self._dry_mass = 0
        else:
            self._config_path = CONFIG_PATH
            self._read_config()

    def _read_config(self):
        with open(self._config_path) as file:
            data = json.load(file)['Parts']['Couplers']

        if self._name not in data.keys():
            raise ValueError(f'{self._name} is not a coupler')
        else:
            data = data[self._name]

        self._dry_mass = data['mass']

    @property
    def dry_mass(self) -> float:
        return self._dry_mass

    @dry_mass.setter
    def dry_mass(self, dry_mass: float) -> None:
        self._dry_mass = dry_mass

    @property
    def exhaust_mass_flow_rate(self) -> float:
        return 0.

    @property
    def isp(self) -> float:
        return 0.

    @property
    def propellant_mass(self) -> float:
        return 0.

    @property
    def thrust(self) -> float:
        return 0.
