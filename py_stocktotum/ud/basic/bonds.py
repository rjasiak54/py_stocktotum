import math


class ZeroCouponBonds:

    def __init__(self, principal: float, maturity: float, interest_rate: float) -> None:
        self.principal = principal
        self.maturity = maturity
        self.interest_rate = interest_rate / 100.0

    def present_value(self, x: float, n: float) -> float:
        return x / (1.0 + self.interest_rate) ** n # type: ignore

    def calculate_price(self) -> float:
        return self.present_value(self.principal, self.maturity)
    
class CouponBond:
    def __init__(self, principal: float, rate: float, maturity: int, interest_rate: float,) -> None:
        self.principal = principal
        self.rate = rate / 100.0
        self.maturity = maturity
        self.interest_rate = interest_rate / 100.0

    def present_value(self, x: float, n: float) -> float:
        return x / (1.0 + self.interest_rate) ** n # type: ignore
    
    def present_value_continuous(self, x: float, n: float) -> float:
        return x / math.e ** (self.interest_rate * n) # type: ignore


    def calculate_price(self) -> float:
        price  = 0.0
        for t in range(1, self.maturity+1):
            price = price + self.present_value(self.principal * self.rate, t)

        price = price + self.present_value(self.principal, self.maturity)

        return price
    
    

    

    
if __name__ == '__main__':
    zbond = ZeroCouponBonds(1000, 2, 4)
    print(f'{zbond.calculate_price():.2f}') 

    cbond = CouponBond(1000, 10, 3, 4 )
    result = (100/0.04) * (1 - (1 / (1.04 ** 3))) + (1000 / (1.04 ** 3))
    print(f'{cbond.calculate_price():.2f} = {result:.2f}') 

    assert 10.0 / math.e ** (2.0) == 10.0 * math.exp(-2.0)