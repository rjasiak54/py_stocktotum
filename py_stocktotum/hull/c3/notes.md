# Hedging Strategies Using Futures

## Terms:
- **Perfect Hedge:** A hedge that eliminates risk completely (These are rare)
- **Daily Settlement:** The amount adjusted in the marging account EOD to account for change in price of the stock
- **Spot Price:** Today/Current price
- **Basis:** basis = (spot price of asset) - (futures price of contract)
- **Hedge Ratio:** The size of the position taken in futures contracts to the size of the exposure


## Oil Producer Example (page 48)
- Current price of oil is $80. The oil producer agreed to sell the oil at the spot-price 3 months from now. He is worried that the price of oil will drop in 3 months. He notices that the 3-month futures price on the market is $79. To hedge his long position (selling oil in 3 months, hoping for the highest price), he shorts by buying future contracts for $79 with the intention of closing them in 3 months.
- The effect of this is that the oil producer locks himself into selling the oil at $79. This is because closing the future contracts throughing buying them back at the spot price will cancel out with the money made from selling the oil at the 3-month spot price. So, the money made is the amount from selling the 3-month futures at $79.


## Basis-of-Risk Notation (page 53):

> To examine the nature of basis risk, we will use the following notation:
    <br>- S<sub>1</sub> : Spot price at time t<sub>1</sub>
    <br>- S<sub>2</sub> : Spot price at time t<sub>2</sub>
    <br>- F<sub>1</sub> : Futures price at time t<sub>1</sub>
    <br>- F<sub>2</sub> : Futures price at time t<sub>2</sub>
    <br>- b<sub>1</sub> : Basis at time t<sub>1</sub>
    <br>- b<sub>2</sub> : Basis at time t<sub>2</sub>

- b<sub>1</sub> = S<sub>1</sub> - F<sub>1</sub>
- b<sub>2</sub> = S<sub>2</sub> - F<sub>2</sub>



## Cross Hedging (page 56)


Let S<sup>\*</sup><sub>2</sub> be the price of asset underlying the futures contract at time t<sub>2</sub>:

- S<sub>2</sub> + F<sub>1</sub> - F<sub>2</sub> = F<sub>1</sub> + b<sub>2</sub> = F<sub>1</sub> + (S<sup>\*</sup><sub>2</sub> - F<sub>2</sub>) + (S<sub>2</sub> - S<sup>*</sup><sub>2</sub>)

### Calculating the Minimum Variance Hedge Ratio

- ∆S: Change in spot price, S, during a period of time equal to the life of the hedge
- ∆F: Change in futures price, F, during a period of time equal to the life of the
hedge.