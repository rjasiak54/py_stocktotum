



def payoff_sell_call(strike: float, k: float) -> float:
    '''
    Giving someone else the right to buy an asset from you

    strike: The excercise price set in the contract
    k:      Delivery price
    '''
    return min(k - strike, 0)

def payoff_buy_put(strike: float, k: float) -> float:
    '''
    Buying the right to sell an asset to someone else
    '''
    return max(k - strike, 0)

def compute_short(future_contract_price: float, real_price_at_end_of_contract: float) -> float:
    '''
    Compute the amount gained or lost from a future contract

    (The price set in the contract minus the real price at the contract execution)
    '''
    return future_contract_price - real_price_at_end_of_contract


def compute_long(future_contract_price: float, real_price_at_end_of_contract: float) -> float:
    return real_price_at_end_of_contract - future_contract_price