import datetime

import numpy as np
import pandas as pd
import yfinance as yf  # type: ignore


def download_data(
    stock: str,
    start_date: datetime.datetime,
    end_date: datetime.datetime,
) -> pd.DataFrame:
    ticker = yf.download(stock, start_date, end_date)
    if ticker is None:
        raise ValueError(f"Ticker is None!!! ticker={stock}")
    return ticker["Close"]  # type: ignore
