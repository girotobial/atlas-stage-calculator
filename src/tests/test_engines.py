from ..parts import engines


def test_LR89_5():
    engine = engines.LR89_5()
    assert engine.dry_mass == 1.75
    assert engine.propellant_mass == 0.
    assert engine.thrust == 205.
    assert engine.isp == 256


def test_LR89_7():
    engine = engines.LR89_7()
    assert engine.dry_mass == 1.75
    assert engine.propellant_mass == 0.
    assert engine.thrust == 236.
    assert engine.isp == 255.


def test_RS56_OBA():
    engine = engines.RS56_OBA()
    assert engine.dry_mass == 1.75
    assert engine.propellant_mass == 0.
    assert engine.thrust == 261.
    assert engine.isp == 263.
