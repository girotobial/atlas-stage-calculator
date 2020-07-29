import pytest
from src.parts import engines
from src.constants import GRAVITATIONAL_ACCELERATION as g



@pytest.mark.parametrize(
    "engine_name, expected_vals",
    [
        ('LR89-5', (205., 1.75, 290)),
        ('LR89-7', (236., 1.75, 294)),
        ('RS56', (261., 1.75, 299))
    ]
)
def test_engine(engine_name, expected_vals):
    engine = engines.Engine(engine_name)
    assert engine.propellant_mass == 0.
    assert engine.thrust == expected_vals[0]
    assert engine.dry_mass == expected_vals[1]
    assert engine.isp == expected_vals[2]
    assert engine.is_composite() is False
    assert engine.exhaust_mass_flow_rate == (
        expected_vals[0] / (g * expected_vals[2])
    )


def test_engine_custom():
    engine = engines.Engine()
    assert engine.dry_mass == 0.
    assert engine.thrust == 0.
    assert engine.isp == 0


def test_engine_not_an_engine():
    with pytest.raises(ValueError, match='not an engine'):
        engines.Engine('Atlas-Long')
