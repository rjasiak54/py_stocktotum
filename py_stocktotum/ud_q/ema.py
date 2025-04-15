import matplotlib.pyplot as plt
import pandas as pd

from py_stocktotum import common


def construct_signals(data: pd.DataFrame, short_period: int, long_period: int) -> None:
    data["Short EMA"] = data["Price"].ewm(span=short_period, adjust=False).mean()
    data["Long EMA"] = data["Price"].ewm(span=long_period, adjust=False).mean()
    # for index, row in data:


# class SmaCrossover:
#     def __init__(self, capital)


if __name__ == "__main__":
    start = "2022-01-01"
    end = "2025-04-14"
    sd = common.yf.download_data("IBM", start, end)
    construct_signals(sd, 30, 50)

    print(sd)
    plt.plot(sd)
    plt.show()
    print()
