from __future__ import annotations
from typing import List
from src.parts.abc_parts import ABCPart
from src.constants import GRAVITATIONAL_ACCELERATION as g


class Stage(ABCPart):
    def __init__(self, name: str = None) -> None:
        self.name = name
        self._parts: List[ABCPart] = []

    def add(self, part: ABCPart) -> None:
        self._parts.append(part)
        part.parent = self

    def remove(self, part: ABCPart) -> None:
        self._parts.remove(part)
        part.parent = None

    def is_composite(self) -> bool:
        return True

    @property
    def thrust(self) -> float:
        return sum([part.thrust for part in self._parts])

    @property
    def dry_mass(self) -> float:
        return sum([part.dry_mass for part in self._parts])

    @property
    def propellant_mass(self) -> float:
        return sum([part.propellant_mass for part in self._parts])

    @property
    def exhaust_mass_flow_rate(self) -> float:
        return sum([part.exhaust_mass_flow_rate for part in self._parts])

    @property
    def isp(self) -> float:
        return self.thrust / (g * self.exhaust_mass_flow_rate)

    def thrust_to_weight_ratio(self, fuel_remaining: float) -> float:
        weight = g * (self.dry_mass + fuel_remaining * self.propellant_mass)
        return self.thrust / weight


class Vehicle(Stage):
    def __init__(self, name: str = None, payload_mass: float = 0.):
        super().__init__(self)
        self.payload_mass = payload_mass

    @property
    def thrust(self):
        return self._parts[0].thrust

    @property
    def isp(self):
        return self._parts[0].isp

    @property
    def dry_mass(self) -> float:
        return sum([part.dry_mass for part in self._parts]) + self.payload_mass

    @property
    def exhaust_mass_flow_rate(self) -> float:
        return self._parts[0].exhaust_mass_flow_rate
