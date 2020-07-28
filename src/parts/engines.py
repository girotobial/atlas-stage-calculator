from src.parts import abc_parts
from src.constants import CONFIG_PATH, GRAVITATIONAL_ACCELERATION
import json


class Engine(abc_parts.ABCPart):
    def __init__(self, name: str):
        self._name = name
        self._read_config()

    def _read_config(self):
        with open(CONFIG_PATH) as file:
            data = json.load(file)["Parts"]["Engines"]

        if self._name not in data.keys():
            raise ValueError(f'{self._name} is not an engine')
        else:
            data = data[self._name]

        self._dry_mass = data['mass']
        self._thrust = data['max_thrust']
        self._surface_isp = data['surface_isp']
        self._vacuum_isp = data['vacuum_isp']

    @property
    def dry_mass(self):
        return self._dry_mass

    @property
    def thrust(self):
        return self._thrust

    @property
    def isp(self):
        return self._vacuum_isp

    @property
    def propellant_mass(self):
        return 0.

    @property
    def exhaust_mass_flow_rate(self):
        g = GRAVITATIONAL_ACCELERATION
        return self.thrust / (g * self.isp)
