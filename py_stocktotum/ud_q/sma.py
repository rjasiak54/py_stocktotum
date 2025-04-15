import matplotlib.pyplot as plt
import pandas as pd

from py_stocktotum import common


def construct_signals(data: pd.DataFrame, short_period: int, long_period: int) -> None:
    data["Short SMA"] = data["Price"].rolling(window=short_period).mean()
    data["Long SMA"] = data["Price"].rolling(window=long_period).mean()


if __name__ == "__main__":
    start = "2010-01-01"
    end = "2020-01-01"
    sd = common.yf.download_data("IBM", start, end)
    construct_signals(sd, 50, 200)

    print(sd)
    plt.plot(sd)
    plt.show()
    print()
