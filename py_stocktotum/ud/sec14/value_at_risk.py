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


def calculate_var_n(
    position: float, c: float, mu: float, sigma: float, n: int
) -> float:
    var: float = position * (mu * n - sigma * np.sqrt(n) * stats.norm.ppf(1 - c))
    return var


if __name__ == "__main__":
    start = datetime.datetime(2014, 1, 1)
    end = datetime.datetime(2018, 1, 1)
    stock_data = download_data("C", start, end)
    stock_data["returns"] = np.log(stock_data["C"] / stock_data["C"].shift(1))

    S = 1e6
    c = 0.99
    mu = np.mean(stock_data["returns"])
    sigma = np.std(stock_data["returns"])
    var = calculate_var_n(S, c, mu, sigma, 100)
    print(f"var: {var}")
