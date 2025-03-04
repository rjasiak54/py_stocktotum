from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

# Market Interest Rate
RISK_FREE_RATE = 0.05
MONTHS_IN_YEAR = 12


class CAPM:
    def __init__(self, stocks: Any, start_date: str, end_date: str) -> None:
        self.stocks = stocks
        self.start_date = start_date
        self.end_date = end_date
        self.data = pd.DataFrame()

    def download_data(self) -> pd.DataFrame:
        data = []
        for stock in self.stocks:
            ticker = yf.download(stock, self.start_date, self.end_date)
            # print(ticker)
            # print(ticker["Close"])
            data.append(ticker["Close"])
        # print(data)
        return pd.concat(data, axis=1)
        # return pd.DataFrame(data)

    def initialize(self) -> None:
        stock_data = self.download_data()
        print(stock_data)
        stock_data = stock_data.resample("M").last()
        print(stock_data)
        self.data = pd.DataFrame(
            {
                "s_adjclose": stock_data[self.stocks[0]],
                "m_adjclose": stock_data[self.stocks[1]],
            }
        )
        self.data[["s_returns", "m_returns"]] = np.log(
            self.data[["s_adjclose", "m_adjclose"]]
            / self.data[["s_adjclose", "m_adjclose"]].shift(1)
        )
        self.data = self.data[1:]
        print(self.data)

    def calculate_beta(self) -> None:
        cov_mat = np.cov(self.data["s_returns"], self.data["m_returns"])
        beta = cov_mat[0, 1] / cov_mat[1, 1]
        print(f"beta: {beta}")

    def regression(self) -> None:
        beta, alpha = np.polyfit(self.data["m_returns"], self.data["s_returns"], deg=1)
        print(f"alpha, beta: {alpha}, {beta}")
        er = RISK_FREE_RATE + beta * (
            self.data["m_returns"].mean() * MONTHS_IN_YEAR - RISK_FREE_RATE
        )
        print(f"Expected return: {er}")
        self.plot_regression(alpha, beta)

    def plot_regression(self, alpha: Any, beta: Any) -> None:
        fix, axis = plt.subplots(1, figsize=(20, 10))
        axis.scatter(
            self.data["m_returns"], self.data["s_returns"], label="Data Points"
        )
        axis.plot(
            self.data["m_returns"],
            beta * self.data["m_returns"] + alpha,
            color="red",
            label="CAPM",
        )
        plt.title("CAPM Pricing Model")
        plt.xlabel("Market return $R_m$", fontsize=18)
        plt.xlabel("Stock return $R_a$", fontsize=10)
        plt.text(0.08, 0.05, r"$R_a = \beta * R_m + \alpha$", fontsize=18)
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    c = CAPM(["IBM", "^GSPC"], "2010-01-01", "2017-01-01")
    c.initialize()
    c.calculate_beta()
    c.regression()
