from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas
import scipy.optimize as opt
import yfinance  # type: ignore

NUM_TRADING_DAYS = 252
NUM_PORTFOLIOS = 10000
stocks = ["AAPL", "WMT", "TSLA", "GE", "AMZN", "DB", "META"]

start_date = "2012-01-01"
end_date = "2017-01-01"


def download_data() -> pandas.DataFrame:
    stock_data = {}

    for stock in stocks:
        ticker = yfinance.Ticker(stock)
        stock_data[stock] = ticker.history(start=start_date, end=end_date)["Close"]

    return pandas.DataFrame(stock_data)


def show_data(data: pandas.DataFrame) -> None:
    data.plot(figsize=(10, 5))
    plt.show()


def calculate_return(data: pandas.DataFrame) -> np.typing.NDArray[Any]:
    log_return = np.log(data / data.shift(1))
    return log_return[1:]


def show_statistics(data: np.typing.NDArray[Any]) -> None:
    print(f"data type: {type(data)}")
    print(data.mean() * NUM_TRADING_DAYS)
    print(data.cov() * NUM_TRADING_DAYS)


def show_mean_variance(
    returns: np.typing.NDArray[Any], weights: np.typing.NDArray[Any]
) -> None:
    pr = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    pv = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))
    print(f"expected portfolio mean (return):                   {pr}")
    print(f"expected portfolio volatility (standard deviation): {pv}")


def show_portfolio(
    returns: np.typing.NDArray[Any], vols: np.typing.NDArray[Any]
) -> None:
    plt.figure(figsize=(10, 6))
    plt.scatter(vols, returns, c=returns / vols, marker="o")
    plt.grid(True)
    plt.xlabel("Expected Volatility")
    plt.ylabel("Expected Return")
    plt.colorbar(label="Sharpe Ratio")
    plt.show()


def generate_portfolios(
    returns: np.typing.NDArray[Any],
) -> tuple[np.typing.NDArray[Any], np.typing.NDArray[Any], np.typing.NDArray[Any]]:
    p_means = []
    p_risks = []
    p_weights = []

    print(f"returns type: {type(returns)}")
    for _ in range(NUM_PORTFOLIOS):
        w = np.random.random(len(stocks))
        w /= np.sum(w)
        p_weights.append(w)
        p_means.append(np.sum(returns.mean() * w) * NUM_TRADING_DAYS)
        p_risks.append(
            np.sqrt(np.dot(w.T, np.dot(returns.cov() * NUM_TRADING_DAYS, w)))
        )
    return np.array(p_weights), np.array(p_means), np.array(p_risks)


def statistics(
    weights: np.typing.NDArray[Any], returns: np.typing.NDArray[Any]
) -> np.typing.NDArray[Any]:
    p_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    p_vol = np.sqrt(
        np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights))
    )
    return np.array([p_return, p_vol, p_return / p_vol])


def min_sharpe(
    weights: np.typing.NDArray[Any], returns: np.typing.NDArray[Any]
) -> np.typing.NDArray[Any]:
    return -statistics(weights, returns)[2]


def optimize_portfolio(
    weights: np.typing.NDArray[Any], returns: np.typing.NDArray[Any]
) -> np.typing.NDArray[Any]:
    constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
    bounds = tuple((0, 1) for _ in range(len(stocks)))
    return opt.minimize(
        fun=min_sharpe,
        x0=weights[0],
        bounds=bounds,
        args=returns,
        method="SLSQP",
        constraints=constraints,
    )
    return np.array([])


def print_portfolio_returns(optimum: Any, returns: Any) -> None:
    print(f"Optimal portfolio: {optimum['x'].round(3)}")
    print(
        f'exepcted return, vol & sharpe ratio: {statistics(optimum["x"].round(3), returns)}'
    )


def show_opt_portfolio(opt: Any, ret: Any, pret: Any, pvol: Any) -> None:
    plt.figure(figsize=(10, 6))
    plt.scatter(pvol, pret, c=pret / pvol, marker="o")
    plt.grid(True)
    plt.xlabel("Expected Volatility")
    plt.ylabel("Expected Return")
    plt.colorbar(label="Sharpe Ratio")
    s = statistics(opt["x"], ret)
    plt.plot(s[1], s[0], "g*", markersize=20)
    plt.show()


if __name__ == "__main__":
    d = download_data()
    r = calculate_return(d)
    print(r)
    show_statistics(r)
    # show_mean_variance(r, )
    # exit(0)
    print(f"r type: {type(r)}")
    weights, means, risks = generate_portfolios(r)
    show_portfolio(means, risks)
    optimum = optimize_portfolio(weights, r)
    print_portfolio_returns(optimum, r)
    show_opt_portfolio(optimum, r, means, risks)
    # show_mean_variance(means, risks)
