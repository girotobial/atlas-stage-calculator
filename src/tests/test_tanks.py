import pytest
from ..parts import tanks


@pytest.mark.parametrize(
    "tank_name, expected_vals",
    [
        ('Atlas-Tapered', (0.175, 3.5)),
        ('Atlas-Long', (0.55, 11))
    ]
)
def test_tank(tank_name: str, expected_vals: tuple):
    tank = tanks.Tank(tank_name)
    # Tanks by definition don't produce thrust
    assert tank.thrust == 0.
    assert tank.isp == 0.
    # Check
    assert tank.dry_mass == expected_vals[0]
    assert tank.propellant_mass == expected_vals[1]
    assert tank.is_composite() is False


def test_tank_error():
    with pytest.raises(ValueError, match='not a fuel tank'):
        tanks.Tank('LR89-5')
