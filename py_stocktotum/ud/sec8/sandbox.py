from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def wiener_process(
    dt: float = 0.1, x0: int = 0, n: int = 1000
) -> tuple[np.typing.NDArray[Any], np.typing.NDArray[Any]]:
    W = np.zeros(n + 1)

    t = np.linspace(x0, n, n + 1)

    W[1 : n + 1] = np.cumsum(np.random.normal(0, np.sqrt(dt), n))

    return t, W


def plot_process(t: np.typing.NDArray[Any], W: np.typing.NDArray[Any]) -> None:
    plt.plot(t, W)
    plt.xlabel("Time(t)")
    plt.ylabel("Wiener-process W(t)")
    plt.title("Wiener-process")
    plt.show()


if __name__ == "__main__":
    time, data = wiener_process()
    plot_process(time, data)
