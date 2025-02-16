import pandas as pd
import numpy as np
# from alpha_vantage.timeseries import TimeSeries # type: ignore
import matplotlib.pyplot as plt

from py_stocktotum.alphvant.timeseries import TimeSeries

async def mac1() -> None:

    # Set your Alpha Vantage API Key
    API_KEY = 'A3KIN32QOLV8SMUL'

    # Initialize the TimeSeries object
    ts = TimeSeries()

    # Get daily stock data for a specific ticker (e.g., Apple)
    ticker = 'SBUX'
    data = await ts.get_daily(symbol=ticker, startdate='2021-01-01')

    # Print first few rows
    # print(data.head())
    print(data)

    w1 = 50
    w2 = 200

    # Plot closing prices
    # data['adjusted_close'].plot()
    # plt.title(f'{ticker} Stock Closing Prices')
    # Calculate Simple Moving Averages (SMA)
    data['SMA_w1'] = data['adjusted_close'].rolling(window=w1).mean()
    data['SMA_w2'] = data['adjusted_close'].rolling(window=w2).mean()

    # Plot SMAs with closing price
    data[['adjusted_close', 'SMA_w1', 'SMA_w2']].plot()
    plt.title(f'{ticker} Stock Closing Prices and SMA')
    # plt.show()

    # Strategy: Generate Buy and Sell signals
    data['Signal'] = 0
    data['Signal'][w1:] = np.where(data['SMA_w1'][w1:] > data['SMA_w2'][w1:], 1, -1)
    data['Position'] = data['Signal'].diff()
    data['Position'] = data['Position'].shift(1)
    print(data[data['Position'] != 0.0])

    # # Print signals
    # # plt.show()
    # # Backtesting: Calculate returns
    # initial_investment = 10000
    # data['Returns'] = data['adjusted_close'].pct_change()
    # data['Strategy_Returns'] = np.where(data['Position'].shift(1) != 0.0, data['Signal'].shift(1) * data['Returns'], 0.0)
    # data['Portfolio_Value'] = initial_investment * (1 + data['Strategy_Returns']).cumprod()

    # data[['Returns', 'Strategy_Returns']].plot()
    # print(data)
    # print(data[data['Position'] != 0.0] )
    # print(data[(data['Strategy_Returns'] != 0.0) | (data['Position'] != 0.0)] )
    # Plot Portfolio Value
    # data['Portfolio_Value'].plot()


    # Initialize portfolio
    initial_investment = 10000
    data['Cash'] = initial_investment
    data['Shares'] = 0
    data['Portfolio_Value'] = initial_investment
    print(data)
    # Simulation parameters
    transaction_cost = 0.01  # 1% transaction fee

    transactions = []

    # Simulate portfolio evolution based on buy/sell signals
    for i in range(1, len(data)):
        if data['Position'].iloc[i] > 0:  # Buy signal
            if data['Cash'].iloc[i-1] > 0:  # Only buy if you have cash available
                print('buying')
                print(data.iloc[i])
                # Buy as many shares as possible with available cash
                data.loc[data.index[i], 'Shares'] = data['Cash'].iloc[i-1] / (data['adjusted_close'].iloc[i-1] * (1 + transaction_cost))
                data.loc[data.index[i], 'Cash'] = 0  # All cash used to buy shares
                # Update portfolio value
                data.loc[data.index[i], 'Portfolio_Value'] = data['Cash'].iloc[i] + data['Shares'].iloc[i] * data['adjusted_close'].iloc[i-1]
                transactions.append(data.iloc[i])
        elif data['Position'].iloc[i] < 0:  # Sell signal
            if data['Shares'].iloc[i-1] > 0:  # Only sell if you have shares
                print("selling")
                print(data.iloc[i].index)
                # Sell all shares
                data.loc[data.index[i], 'Cash'] = data['Shares'].iloc[i-1] * data['adjusted_close'].iloc[i-1] * (1 - transaction_cost)
                data.loc[data.index[i], 'Shares'] = 0  # Sold all shares
                # Update portfolio value
                data.loc[data.index[i], 'Portfolio_Value'] = data['Cash'].iloc[i] + data['Shares'].iloc[i] * data['adjusted_close'].iloc[i-1]
                transactions.append(data.iloc[i])
            else:
                print('no shares!')
        else:  # Hold the position (no new signal)
            # Carry forward the cash and shares from the previous day
            data.loc[data.index[i], 'Cash'] = data['Cash'].iloc[i-1]
            data.loc[data.index[i], 'Shares'] = data['Shares'].iloc[i-1]

        # Update portfolio value
        data.loc[data.index[i], 'Portfolio_Value'] = data['Cash'].iloc[i] + data['Shares'].iloc[i] * data['adjusted_close'].iloc[i]

    print(data.iloc[w1:])
    # Plot portfolio value over time
    print(pd.DataFrame(transactions))
    print(f"Final Portfolio Value: ${data['Portfolio_Value'].iloc[-1]:.2f}")
    # plt.plot(data['Portfolio_Value'], label='Portfolio Value')
    plt.show()
    # plt.title(f'{ticker} Portfolio Value Over Time')
    # plt.xlabel('Date')
    # plt.ylabel('Portfolio Value ($)')
    # plt.legend()
    # plt.show()



    plt.title(f'{ticker} Portfolio Value based on Moving Average Crossover Strategy')
    # plt.show()
