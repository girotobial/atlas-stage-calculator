import pytest
from ..parts import engines


@pytest.mark.parametrize(
    "engine_name, expected_vals",
    [
        ('LR89-5', (205., 1.75, 256)),
        ('LR89-7', (236., 1.75, 255)),
        ('RS56', (261., 1.75, 263))
    ]
)
def test_engine(engine_name, expected_vals):
    engine = engines.Engine(engine_name)
    assert engine.propellant_mass == 0.
    assert engine.thrust == expected_vals[0]
    assert engine.dry_mass == expected_vals[1]
    assert engine.isp == expected_vals[2]

