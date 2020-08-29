import json
from src.parts import abc_parts
from src.constants import LIQUID_FUEL_DENSITY, OXIDISER_DENSITY, CONFIG_PATH


class Tank(abc_parts.ABCPart):
    def __init__(self, name: str = 'Custom'):
        self._name = name
        self._propellant_mass = None
        if self._name == 'Custom':
            self._dry_mass = 0.
            self._oxidiser_volume = 0.
            self._fuel_volumne = 0.
        else:
            self._read_config()

    def _read_config(self):
        with open(CONFIG_PATH) as file:
            data = json.load(file)['Parts']['Tanks']

        if self._name not in data.keys():
            raise ValueError(f'{self._name} is not a fuel tank')
        else:
            data = data[self._name]

        self._dry_mass = data['mass']
        self._oxidiser_volume = data['max_oxidiser_volume']
        self._fuel_volumne = data['max_fuel_volume']

    @property
    def dry_mass(self) -> float:
        return self._dry_mass

    @dry_mass.setter
    def dry_mass(self, dry_mass: float):
        self._dry_mass = dry_mass

    @property
    def thrust(self) -> float:
        return 0

    @property
    def isp(self) -> float:
        return 0

    @property
    def propellant_mass(self) -> float:
        if self._propellant_mass:
            return self._propellant_mass
        else:
            oxidiser_mass = self._oxidiser_volume * OXIDISER_DENSITY
            fuel_mass = self._fuel_volumne * LIQUID_FUEL_DENSITY
            self._propellant_mass = fuel_mass + oxidiser_mass
        return self._propellant_mass

    @propellant_mass.setter
    def propellant_mass(self, propellant_mass: float):
        self._propellant_mass = propellant_mass

    @property
    def exhaust_mass_flow_rate(self) -> float:
        return 0.
