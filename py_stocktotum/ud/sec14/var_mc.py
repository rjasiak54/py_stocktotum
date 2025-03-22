# VaR
import datetime

import numpy as np
import pandas as pd
import yfinance as yf  # type: ignore
from scipy import stats


def download_data(
    stock: str,
    start_date: datetime.datetime,
    end_date: datetime.datetime,
) -> pd.DataFrame:
    ticker = yf.download(stock, start_date, end_date)
    if ticker is None:
        raise ValueError(f"Ticker is None!!! ticker={stock}")
    return ticker["Close"]  # type: ignore


class ValueAtRiskMonteCarlo:
    def __init__(
        self,
        S: float,
        mu: float,
        sigma: float,
        c: float,
        n: int,
        iterations: int,
    ) -> None:
        self.S = S
        self.mu = mu
        self.sigma = sigma
        self.c = c
        self.n = n
        self.iterations = iterations

    def simulation(self) -> np.float64:
        rand = np.random.normal(0, 1, [1, self.iterations])
        stock_price = self.S * np.exp(
            self.n * (self.mu - 0.5 * self.sigma**2)
            + self.sigma * np.sqrt(self.n) * rand
        )
        stock_price = np.sort(stock_price)

        percentile: np.float64 = np.percentile(stock_price, (1 - self.c) * 100)

        return self.S - percentile


if __name__ == "__main__":
    S = 1e6
    c = 0.95
    n = 1
    iterations = 100000
    start_date = datetime.datetime(2014, 1, 1)
    end_date = datetime.datetime(2017, 10, 15)
    citi = download_data("C", start_date, end_date)
    citi["returns"] = citi.pct_change()
    mu = np.mean(citi["returns"])
    sigma = np.std(citi["returns"])
    model = ValueAtRiskMonteCarlo(S, mu, sigma, c, n, iterations)
    var = model.simulation()
    print(f"var: {var}")
