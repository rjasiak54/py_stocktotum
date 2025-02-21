import math


def future_discrete_value(present_money: float, interest_rate: float, years: int) -> float:
    return present_money * (1 + interest_rate) ** years


def present_discrete_value(future_money: float, interest_rate: float, years: int) -> float:
    return future_money * (1 + interest_rate) ** -years


def future_continuous_value(present_money: float, interest_rate: float, time: float) -> float:
    return present_money * math.exp(interest_rate * time)


def present_continuous_value(future_money: float, interest_rate: float, time: float) -> float:
    return future_money * math.exp(-interest_rate * time)
