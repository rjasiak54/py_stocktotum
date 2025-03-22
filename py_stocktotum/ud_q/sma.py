import matplotlib.pyplot as plt

from py_stocktotum import common

if __name__ == "__main__":
    start = "2010-01-01"
    end = "2020-01-01"
    sd = common.yf.download_data("IBM", start, end)
    print(sd)
    plt.plot(sd)
    plt.show()
    print()
