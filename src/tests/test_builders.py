import json
import pytest
import src.builders
import src.parts
from src.constants import CONFIG_PATH

config = json.load(open(CONFIG_PATH))


# Stage Builder tests
def test_stagebuilder_init():
    builder = src.builders.StageBuilder()
    assert type(builder._stage) is src.parts.Stage


@pytest.mark.parametrize(
    "tank_str",
    [
        tank
        for tank
        in config['Parts']['Tanks'].keys()
    ]
)
def test_stagebuilder_add_tanks_success(tank_str):
    # Setup
    builder = src.builders.StageBuilder()

    # Test method return correct type
    builder._add_tanks([tank_str])
    assert type(builder._stage._parts[0]) is src.parts.Tank

    # Test attributes of returned engine match calling Tank class directly
    correct_tank = src.parts.Tank(tank_str)
    test_tank = builder._stage._parts[0]

    assert test_tank.dry_mass == correct_tank.dry_mass
    assert test_tank.propellant_mass == correct_tank.propellant_mass
    assert test_tank.thrust == correct_tank.thrust
    assert test_tank.isp == correct_tank.isp
    assert (test_tank.exhaust_mass_flow_rate ==
            correct_tank.exhaust_mass_flow_rate)
    assert test_tank.is_composite() == correct_tank.is_composite()


@pytest.mark.parametrize(
    "engine_str",
    [
        engine
        for engine
        in config['Parts']['Engines'].keys()
    ]
)
def test_stagebuilder_add_engines_success(engine_str):
    # Setup
    builder = src.builders.StageBuilder()

    # Test method returns correct type
    builder._add_engines([engine_str])
    assert type(builder._stage._parts[0]) is src.parts.Engine

    # Test attributes of returned engine match calling Engine object directly
    correct_engine = src.parts.Engine(engine_str)
    test_engine = builder._stage._parts[0]

    assert test_engine.dry_mass == correct_engine.dry_mass
    assert test_engine.propellant_mass == correct_engine.propellant_mass
    assert test_engine.thrust == correct_engine.thrust
    assert test_engine.isp == correct_engine.isp
    assert (test_engine.exhaust_mass_flow_rate ==
            correct_engine.exhaust_mass_flow_rate)
    assert test_engine.is_composite() == correct_engine.is_composite()


@pytest.mark.parametrize(
    "coupler_str",
    [
        coupler
        for coupler
        in config['Parts']['Couplers'].keys()
    ]
)
def test_stagebuilder_add_couplers_success(coupler_str):
    # Setup
    builder = src.builders.StageBuilder()

    # Test method returns correct type
    builder._add_couplers([coupler_str])
    assert type(builder._stage._parts) is src.parts.Coupler

    # Test attributes of returned engine match calling Coupler class directly
    correct_coupler = src.parts.Coupler(coupler_str)
    test_coupler = builder._stage._parts[0]

    assert test_coupler.dry_mass == correct_coupler.dry_mass
    assert test_coupler.propellant_mass == correct_coupler.propellant_mass
    assert test_coupler.thrust == correct_coupler.thrust
    assert test_coupler.isp == correct_coupler.isp
    assert (test_coupler.exhaust_mass_flow_rate ==
            correct_coupler.exhaust_mass_flow_rate)
    assert test_coupler.is_composite() == correct_coupler.is_composite()


def test_stage_builder_build_standard_not_standard():
    builder = src.builders.StageBuilder()
    with pytest.raises(ValueError, match="is not a standard stage"):
        builder.build_standard('lol not a rocket')


# Vehicle Builder Tests
def test_vehicle_builder_init():
    builder = src.builders.VehicleBuilder()
    assert type(builder._stage_builder) is src.builders.StageBuilder
    assert type(builder._vehicle) is src.parts.Vehicle


def test_vehicle_builder_product():
    builder = src.builders.VehicleBuilder()

    # Check builder product is a Vehicle
    assert type(builder.product) is src.parts.Vehicle

    # Check builder product resets
    test_vehicle = src.parts.Vehicle(name='test', payload_mass=1)
    builder._vehicle = test_vehicle
    # Should be the same on first call
    assert builder.product == test_vehicle
    # Should now be reset
    assert builder.product != test_vehicle


def test_vehicle_builder_reset():
    builder = src.builders.VehicleBuilder()
    test_vehicle = src.parts.Vehicle('test', 1)

    builder._vehicle = test_vehicle
    assert builder._vehicle == test_vehicle
    builder.reset()
    assert builder._vehicle != test_vehicle


def test_vehicle_builder_build_standard_not_standard():
    builder = src.builders.VehicleBuilder()
    with pytest.raises(ValueError, match="is not a standard vehicle"):
        builder.build_standard('lol not a rocket')
