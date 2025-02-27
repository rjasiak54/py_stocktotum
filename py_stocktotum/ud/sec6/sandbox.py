from typing import Any

import numpy as np
import pandas
import yfinance
import matplotlib.pyplot as plt

NUM_TRADING_DAYS = 252
NUM_PORTFOLIOS = 10000
stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']

start_date = '2012-01-01'
end_date = '2017-01-01'

def download_data() -> pandas.DataFrame:
    stock_data = {}

    for stock in stocks:
        ticker = yfinance.Ticker(stock)
        stock_data[stock]  = ticker.history(start=start_date, end=end_date)['Close']

    return pandas.DataFrame(stock_data)


def show_data(data: pandas.DataFrame) -> None:
    data.plot(figsize=(10,5))
    plt.show()

def calculate_return(data: pandas.DataFrame) -> np.typing.NDArray[Any]:
    log_return = np.log(data/data.shift(1))
    return log_return[1:]

def show_statistics(data: np.typing.NDArray[Any]) -> None:
    print(data.mean() * NUM_TRADING_DAYS)
    print(data.cov() * NUM_TRADING_DAYS)

def show_mean_variance(returns: np.typing.NDArray[Any], weights: np.typing.NDArray[Any]) -> None:
    pr = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    pv = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))
    print(f'expected portfolio mean (return):                   {pr}')
    print(f'expected portfolio volatility (standard deviation): {pv}')


def generate_portfolios(returns: np.typing.NDArray[Any]) -> None:
    p_means = []
    p_risks = []
    p_weights = []

    for _ in range(NUM_PORTFOLIOS):
        w = np.random.random(len(stocks))

if __name__ == '__main__':
    d = download_data()
    r = calculate_return(d)
    print(r)
    show_statistics(r)
    show_mean_variance(r, )
    # show_data(d)