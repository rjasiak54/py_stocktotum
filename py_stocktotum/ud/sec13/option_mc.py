import numpy as np


class OptionPricing:

    def __init__(
        self,
        S0: float,
        E: float,
        T: float,
        rf: float,
        sigma: float,
        iterations: int,
    ) -> None:
        self.S0 = S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.iterations = iterations

    def call_option_simulation(self) -> np.float64:
        option_data = np.zeros([self.iterations, 2])
        rand = np.random.normal(0, 1, [1, self.iterations])
        stock_price = self.S0 * np.exp(
            self.T * (self.rf - 0.5 * self.sigma**2)
            + self.sigma * np.sqrt(self.T) * rand
        )
        option_data[:, 1] = stock_price - self.E

        average = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)

        price: np.float64 = np.exp(-1.0 * self.rf * self.T) * average
        return price

    def put_option_simulation(self) -> np.float64:
        option_data = np.zeros([self.iterations, 2])
        rand = np.random.normal(0, 1, [1, self.iterations])
        stock_price = self.S0 * np.exp(
            self.T * (self.rf - 0.5 * self.sigma**2)
            + self.sigma * np.sqrt(self.T) * rand
        )
        option_data[:, 1] = self.E - stock_price

        average = np.sum(np.amax(option_data, axis=1)) / float(self.iterations)

        price: np.float64 = np.exp(-1.0 * self.rf * self.T) * average
        return price


if __name__ == "__main__":
    model = OptionPricing(100, 100, 1, 0.05, 0.2, 1000)
    cp = model.call_option_simulation()
    pp = model.put_option_simulation()
    print(f"cp: {cp}")
    print(f"pp: {pp}")
