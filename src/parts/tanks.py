from . import abc_parts
from ..constants import LIQUID_FUEL_DENSITY, OXIDISER_DENSITY


class BaseTank(abc_parts.ABCPart):
    def __init__(self):
        self._dry_mass = None
        self._liquid_fuel_volume = None
        self._oxidiser_volume = None

    @property
    def dry_mass(self):
        return self._dry_mass

    @property
    def thrust(self):
        return 0.

    @property
    def isp(self):
        return 0.

    @property
    def propellant_mass(self):
        fuel_mass = self._liquid_fuel_volume * LIQUID_FUEL_DENSITY
        oxidiser_mass =  self._oxidiser_volume * OXIDISER_DENSITY
        return fuel_mass + oxidiser_mass


class TaperedTank(BaseTank):
    '''
    Atlas-700 Balloon Fuel Tank

    0.9375m / 1.25m adapter fuel tank for the Atlas 1.875m launcher
    '''
    def __init__(self):
        super().__init__()
        self._dry_mass = 0.175
        self._liquid_fuel_volume = 315.
        self._oxidiser_volume = 385.


class 