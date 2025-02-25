from . import basic


def main() -> None:
    m = 100
    r = 0.05
    y = 5
    result = basic.future_discrete_value(m, r, y)
    print(f'fdv:  {m} * (1 + {r})^{y}   = {result}')

    result = basic.present_discrete_value(m, r, y)
    print(f'pdv:  {m} * (1 + {r})^-{y}  = {result}')

    result = basic.future_continuous_value(m, r, y)
    print(f'fcv:  {m} * e^rt            = {result}')

    result = basic.present_continuous_value(m, r, y)
    print(f'pcv:  {m} * e^-rt           = {result}')



if __name__ == '__main__':
    main()