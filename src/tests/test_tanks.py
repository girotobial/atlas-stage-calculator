import pytest
from ..parts import tanks


@pytest.mark.parametrize(
    "tank, expected_vals",
    [
        (tanks.TaperedTank, (0.175, 3500))
    ]
)
def test_tank(tank: tanks.BaseTank, expected_vals: tuple):
    tank = tank()
    # Tanks by definition don't produce thrust
    assert tank.thrust == 0.
    assert tank.isp == 0.

    assert tank.dry_mass == expected_vals[0]
    assert tank.propellant_mass == expected_vals[1]
