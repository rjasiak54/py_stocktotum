import math

from . import basic


def main() -> None:
    m = 1000
    r = 0.04
    y = 3
    result = basic.future_discrete_value(m, r, y)
    print(f'fdv:  {m} * (1 + {r})^{y}   = {result}')

    result = basic.present_discrete_value(m, r, y)
    print(f'pdv:  {m} * (1 + {r})^-{y}  = {result}')

    result = basic.future_continuous_value(m, r, y)
    print(f'fcv:  {m} * e^rt            = {result}')

    result = basic.present_continuous_value(m, r, y)
    print(f'pcv:  {m} * e^-rt           = {result}')

    result = (100/0.04) * (1 - (1 / (1.04 ** 3))) + (1000 / (1.04 ** 3))
    print(result)
    print()

    _e = sum([1 / math.factorial(i) for i in range(100)])
    print(f'Value of e: {_e}')

if __name__ == '__main__':
    main()