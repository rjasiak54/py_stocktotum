from . import options
import math


def test__1_5() -> None:
    n_units = 10 ** 5
    contract_price = 1.9

    a = options.compute_short(contract_price, 1.89) * n_units
    assert math.isclose(a, 1000)

    b = options.compute_short(contract_price, 1.92) * n_units
    assert math.isclose(b, -2000)


def test__1_6() -> None:
    n_units = 5 * 10 ** 4
    contract_price = .5

    a = options.compute_short(contract_price, 0.482) * n_units
    assert math.isclose(a, 900)

    a = options.compute_short(contract_price, 0.513) * n_units
    assert math.isclose(a, -650)