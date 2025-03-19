import datetime

import numpy as np
import pandas as pd
import yfinance as yf  # type: ignore


def download_data(
    stock: str,
    start_date: datetime.datetime | str,
    end_date: datetime.datetime | str,
) -> pd.DataFrame:
    ticker = yf.download(stock, start_date, end_date)
    if ticker is None:
        raise ValueError(f"Ticker is None!!! ticker={stock}")
    ret = pd.DataFrame()
    ret["Price"] = ticker["Close"]

    return ret
