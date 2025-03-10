from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def simulate_geometric_random_walk(
    S0: float,
    T: int = 2,
    N: int = 1000,
    mu: float = 0.1,
    sigma: float = 0.05,
) -> tuple[np.typing.NDArray[Any], Any]:
    dt = T / N
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W) * np.sqrt(dt)
    X = (mu - 0.5 * sigma**2) * t + sigma * W
    S = S0 * np.exp(X)
    return t, S


def plot_simulation(t: np.typing.NDArray[Any], S: Any) -> None:
    plt.plot(t, S)
    plt.xlabel("Time (t)")
    plt.ylabel("Stock Price S(t)")
    plt.title("Geometric Brownian Motion")
    plt.show()


if __name__ == "__main__":
    t, S = simulate_geometric_random_walk(10)
    plot_simulation(t, S)
