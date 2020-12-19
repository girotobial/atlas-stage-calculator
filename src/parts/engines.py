import json

from src.constants import CONFIG_PATH, GRAVITATIONAL_ACCELERATION
from src.parts import abc_parts


class Engine(abc_parts.ABCPart):
    def __init__(self, name: str = "Custom"):
        self._name = name
        if name == "Custom":
            self._dry_mass = 0.0
            self._thrust = 0.0
            self._surface_isp = 0.0
            self._vacuum_isp = 0.0
        else:
            self._config_path = CONFIG_PATH
            self._read_config()

    def _read_config(self):
        with open(self._config_path) as file:
            data = json.load(file)["Parts"]["Engines"]

        if self._name not in data.keys():
            raise ValueError(f"{self._name} is not an engine")
        else:
            data = data[self._name]

        self._dry_mass = data["mass"]
        self._thrust = data["max_thrust"]
        self._surface_isp = data["surface_isp"]
        self._vacuum_isp = data["vacuum_isp"]

    @property
    def dry_mass(self) -> float:
        return self._dry_mass

    @dry_mass.setter
    def dry_mass(self, dry_mass: float) -> None:
        self._dry_mass = dry_mass

    @property
    def thrust(self) -> float:
        return self._thrust

    @thrust.setter
    def thrust(self, thrust: float):
        self._thrust = thrust

    @property
    def isp(self) -> float:
        return self._vacuum_isp

    @isp.setter
    def isp(self, isp: float):
        self._vacuum_isp = isp

    @property
    def propellant_mass(self) -> float:
        return 0.0

    @property
    def exhaust_mass_flow_rate(self) -> float:
        g = GRAVITATIONAL_ACCELERATION
        return self.thrust / (g * self.isp)
