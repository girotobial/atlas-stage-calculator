import pytest
import src.parts as parts
from src.constants import GRAVITATIONAL_ACCELERATION as g


# Tank Tests
@pytest.mark.parametrize(
    "tank_name, expected_vals",
    [
        ('Atlas-Tapered', (0.175, 3.5)),
        ('Atlas-Long', (0.55, 11))
    ]
)
def test_tank(tank_name: str, expected_vals: tuple):
    tank = parts.Tank(tank_name)
    # Tanks by definition don't produce thrust
    assert tank.thrust == 0.
    assert tank.isp == 0.
    assert tank.exhaust_mass_flow_rate == 0.
    # Check
    assert tank.dry_mass == expected_vals[0]
    assert tank.propellant_mass == expected_vals[1]
    assert tank.is_composite() is False


def test_tank_custom():
    tank = parts.Tank()
    assert tank._tank_name == 'Custom'
    assert tank.thrust == 0.
    assert tank.propellant_mass == 0.


def test_tank_error():
    with pytest.raises(ValueError, match='not a fuel tank'):
        parts.Tank('LR89-5')


def test_tank_setters():
    tank = parts.Tank()

    assert tank.dry_mass == 0
    tank.dry_mass = 1
    assert tank.dry_mass == 1

    assert tank.propellant_mass == 0
    tank.propellant_mass = 1
    assert tank.propellant_mass == 1


# Engine tests
@pytest.mark.parametrize(
    "engine_name, expected_vals",
    [
        ('LR89-5', (205., 1.75, 290)),
        ('LR89-7', (236., 1.75, 294)),
        ('RS56', (261., 1.75, 299))
    ]
)
def test_engine(engine_name, expected_vals):
    engine = parts.Engine(engine_name)
    assert engine.propellant_mass == 0.
    assert engine.thrust == expected_vals[0]
    assert engine.dry_mass == expected_vals[1]
    assert engine.isp == expected_vals[2]
    assert engine.is_composite() is False
    assert engine.exhaust_mass_flow_rate == (
        expected_vals[0] / (g * expected_vals[2])
    )


def test_engine_custom():
    engine = parts.Engine()
    assert engine.dry_mass == 0.
    assert engine.thrust == 0.
    assert engine.isp == 0


def test_engine_not_an_engine():
    with pytest.raises(ValueError, match='not an engine'):
        parts.Engine('Atlas-Long')


def test_engine_setters():
    engine = parts.Engine()
    assert engine.dry_mass == 0.
    engine.dry_mass = 1.
    assert engine.dry_mass == 1.

    assert engine.isp == 0.
    engine.isp = 1.
    assert engine.isp == 1.

    assert engine.thrust == 0.
    engine.thrust = 1.
    assert engine.thrust == 1.
