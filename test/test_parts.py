import pytest

import src.parts as parts
from src.constants import GRAVITATIONAL_ACCELERATION as g


# Base Class Test
@pytest.fixture
def concrete_abc():
    abc = parts.abc_parts.ABCPart
    abc.__abstractmethods__ = set()
    return abc


def test_abc_methods(concrete_abc):
    c_abc = concrete_abc()
    assert c_abc.add(concrete_abc) is None
    assert c_abc.remove(concrete_abc) is None
    assert c_abc.is_composite() is False
    assert c_abc.dry_mass is None
    assert c_abc.propellant_mass is None
    assert c_abc.thrust is None
    assert c_abc.isp is None
    assert c_abc.exhaust_mass_flow_rate is None


def test_abc_parent(concrete_abc):
    cabc = concrete_abc()
    cabc_parent = concrete_abc()
    cabc.parent = cabc_parent
    assert cabc.parent is cabc_parent


# Tank Tests
@pytest.mark.parametrize(
    "name, expected_vals", [("Atlas-Tapered", (0.175, 3.5)), ("Atlas-Long", (0.55, 11))]
)
def test_tank(name: str, expected_vals: tuple):
    tank = parts.Tank(name)
    # Tanks by definition don't produce thrust
    assert tank.thrust == 0.0
    assert tank.isp == 0.0
    assert tank.exhaust_mass_flow_rate == 0.0
    # Check
    assert tank.dry_mass == expected_vals[0]
    assert tank.propellant_mass == expected_vals[1]
    assert tank.is_composite() is False


def test_tank_custom():
    tank = parts.Tank()
    assert tank._name == "Custom"
    assert tank.thrust == 0.0
    assert tank.propellant_mass == 0.0


def test_tank_error():
    with pytest.raises(ValueError, match="not a fuel tank"):
        parts.Tank("LR89-5")


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
        ("LR89-5", (205.0, 1.75, 290)),
        ("LR89-7", (236.0, 1.75, 294)),
        ("RS56", (261.0, 1.75, 299)),
    ],
)
def test_engine(engine_name, expected_vals):
    engine = parts.Engine(engine_name)
    assert engine.propellant_mass == 0.0
    assert engine.thrust == expected_vals[0]
    assert engine.dry_mass == expected_vals[1]
    assert engine.isp == expected_vals[2]
    assert engine.is_composite() is False
    assert engine.exhaust_mass_flow_rate == (expected_vals[0] / (g * expected_vals[2]))


def test_engine_custom():
    engine = parts.Engine()
    assert engine.dry_mass == 0.0
    assert engine.thrust == 0.0
    assert engine.isp == 0


def test_engine_not_an_engine():
    with pytest.raises(ValueError, match="not an engine"):
        parts.Engine("Atlas-Long")


def test_engine_setters():
    engine = parts.Engine()
    assert engine.dry_mass == 0.0
    engine.dry_mass = 1.0
    assert engine.dry_mass == 1.0

    assert engine.isp == 0.0
    engine.isp = 1.0
    assert engine.isp == 1.0

    assert engine.thrust == 0.0
    engine.thrust = 1.0
    assert engine.thrust == 1.0


# accessory tests
@pytest.fixture
def accessory():
    return parts.Accessory()


def test_accessory_properties(accessory):
    assert accessory.dry_mass == 0
    assert accessory.exhaust_mass_flow_rate == 0
    assert accessory.isp == 0
    assert accessory.propellant_mass == 0
    assert accessory.thrust == 0
    assert accessory.is_composite() is False


def test_accessory_setters(accessory):
    assert accessory.dry_mass == 0
    accessory.dry_mass = 1
    assert accessory.dry_mass == 1


@pytest.mark.parametrize(
    "accessory_name, expected_vals",
    [
        ("Atlas-BoosterSkirt", 0.8),
        ("Vanguard-4688 Fairing", 0.05),
    ],
)
def test_accessory_config_read_config(accessory_name, expected_vals):
    accessory = parts.Accessory(accessory_name)
    assert accessory.dry_mass == expected_vals


def test_accessory_not_a_accessory():
    with pytest.raises(ValueError, match="not an accessory"):
        parts.Accessory("FooBar")


# Assembly Tests
@pytest.fixture
def engine():
    engine = parts.Engine()
    engine.dry_mass = 1
    engine.thrust = 2
    engine.isp = 1
    return engine


@pytest.fixture
def tank():
    tank = parts.Tank()
    tank.dry_mass = 1
    tank.propellant_mass = 1
    return tank


def test_stage_construction(tank):
    stage = parts.Stage()
    stage.add(tank)
    assert tank in stage._parts
    assert tank.parent == stage

    stage.remove(tank)
    assert tank not in stage._parts
    assert tank.parent is None


@pytest.fixture
def stage(engine, tank):
    stage = parts.Stage()
    stage.add(engine.copy())
    stage.add(engine.copy())
    stage.add(tank.copy())
    return stage


def test_stage_calculations(stage):
    assert stage.dry_mass == 3.0
    assert stage.propellant_mass == 1.0
    assert stage.thrust == 4.0
    assert stage.isp == 1.0
    assert stage.exhaust_mass_flow_rate == stage.thrust / (g * stage.isp)


def test_stage_composite(stage):
    assert stage.is_composite() is True


@pytest.mark.parametrize(
    "fuel_remaining, expected_value",
    [(1, 4.0 / (4 * g)), (0.75, 4.0 / (3.75 * g)), (0, 4.0 / (3 * g))],
)
def test_stage_twr(stage, fuel_remaining, expected_value):
    assert stage.thrust_to_weight_ratio(fuel_remaining) == expected_value


def test_vehicle_calculations(stage):
    vehicle = parts.Vehicle()
    stage1 = stage.copy()
    stage1._parts[0].thrust = 3
    stage2 = stage
    vehicle.add(stage1)
    vehicle.add(stage2)

    assert vehicle.dry_mass == 6.0
    assert vehicle.propellant_mass == 2.0
    assert vehicle.thrust == 5.0
    assert vehicle.isp == 1.0
    assert vehicle.exhaust_mass_flow_rate == stage1.exhaust_mass_flow_rate
    assert vehicle.thrust_to_weight_ratio(1) == vehicle.thrust / (
        g * (vehicle.dry_mass + vehicle.propellant_mass)
    )
    assert vehicle.mass == 8


def test_add_parent(stage):
    vehicle = parts.Vehicle
    stage.parent = vehicle

    assert stage.parent == vehicle


def test_vehicle_name():
    name = "name"
    vehicle = parts.Vehicle(name)
    assert vehicle.name == name
    new_name = "new name"
    vehicle.name = new_name
    assert vehicle.name == new_name
