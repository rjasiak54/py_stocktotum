import numpy as np
from scipy import stats


def call_options_price(S: float, E: float, T: float, rf: float, sigma: float) -> float:
    d1 = np.log(S / E) + (rf + sigma**2 / 2) * T / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    price: float = S * stats.norm.cdf(d1) - E * np.exp(-rf * T) * stats.norm.cdf(d2)
    return price


def put_options_price(
    S: float, E: float, T: float, rf: float, sigma: float
) -> np.float64:
    d1 = np.log(S / E) + (rf + sigma**2 / 2) * T / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    price: np.float64 = -S * stats.norm.cdf(-d1) + E * np.exp(-rf * T) * stats.norm.cdf(
        -d2
    )
    return price


if __name__ == "__main__":
    S0 = 100
    E = 100
    T = 1
    rf = 0.05
    sigma = 0.2
    call_options_price(S0, E, T, rf, sigma)
    put_options_price(S0, E, T, rf, sigma)
