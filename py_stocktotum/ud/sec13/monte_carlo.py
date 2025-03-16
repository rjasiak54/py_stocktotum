import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

NUM_SIMULATIONS = 100


def stock_monte_carlo(S0: float, mu: float, sigma: float, N: int = 252) -> None:
    result = []
    for _ in range(NUM_SIMULATIONS):
        prices = [S0]
        for _ in range(N):
            stock_price = prices[-1] * np.exp(
                (mu - 0.5 * sigma**2) + sigma * np.random.normal()
            )
            prices.append(stock_price)

        result.append(prices)
    sim_data = pd.DataFrame(result).T

    sim_data["mean"] = sim_data.mean(axis=1)
    plt.plot(sim_data["mean"])
    print(sim_data)
    plt.show()


if __name__ == "__main__":
    stock_monte_carlo(50, 0.0002, 0.01)
