"""
Base classes for parts

"""
from __future__ import annotations

import abc
import copy
from typing import Optional


class ABCPart(abc.ABC):
    """
    The base Part class
    """

    @property
    def parent(self) -> Optional[ABCPart]:
        return self._parent

    @parent.setter
    def parent(self, parent: Optional[ABCPart]) -> None:
        self._parent = parent

    def add(self, part: ABCPart) -> None:
        pass

    def remove(self, part: ABCPart) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    def copy(self) -> ABCPart:
        return copy.deepcopy(self)

    @abc.abstractproperty
    def dry_mass(self) -> float:
        pass

    @abc.abstractproperty
    def propellant_mass(self) -> float:
        pass

    @abc.abstractproperty
    def thrust(self) -> float:
        pass

    @abc.abstractproperty
    def isp(self) -> float:
        pass

    @abc.abstractproperty
    def exhaust_mass_flow_rate(self) -> float:
        pass
