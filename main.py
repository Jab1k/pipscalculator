from xauusd import getGoldPrice

# Function to calculate pips
def calculate_pips(entry_price, exit_price, pair):
    """
    Calculate the pip difference between the entry and exit price.

    Args:
        entry_price (float): The price at which the trade was opened.
        exit_price (float): The price at which the trade was closed.
        pair (str): Currency pair (e.g., 'EURUSD', 'USDJPY', 'XAUUSD', 'BTCUSD').

    Returns:
        float: The number of pips gained or lost.
    """
    # Define pip values based on the currency pair
    if "JPY" in pair:
        pip_value = 0.01
    elif "XAU" in pair or "BTC" in pair:
        pip_value = 0.01  # Similar pip value for Gold and Bitcoin
    else:
        pip_value = 0.0001

    # Calculate the pip difference
    pips = (exit_price - entry_price) / pip_value
    return round(pips, 2)


# Function to calculate pip value based on lot size
def calculate_pip_value(pips, lot_size, pair, exchange_rate=1.0):
    """
    Calculate the value of the pips gained or lost in a trade.

    Args:
        pips (float): The number of pips gained or lost.
        lot_size (float): The lot size of the trade.
        pair (str): Currency pair (e.g., 'EURUSD', 'USDJPY', 'XAUUSD', 'BTCUSD').
        exchange_rate (float): Exchange rate to convert to the account's base currency. Default is 1.0.

    Returns:
        float: The pip value in the account's base currency.
    """
    # Define pip value per lot based on the currency pair
    if "JPY" in pair:
        pip_value_per_lot = 1000  # For JPY pairs
    elif "XAU" in pair:
        pip_value_per_lot = 1  # For XAU/USD, $1 per pip for standard lot
    elif "BTC" in pair:
        pip_value_per_lot = 0.01  # For BTC/USD, $0.01 per pip for standard lot
    else:
        pip_value_per_lot = 10  # For other pairs

    # Calculate the pip value for the given lot size
    pip_value = pips * pip_value_per_lot * lot_size * exchange_rate
    return round(pip_value, 2)


# Example usage
def main():
    try:
        xauusd = getGoldPrice()
        entry = float(input("Kirish zonani kiriting: "))
        exit = float(input(f"Chiqish zonasini kiriting (xozirda XAUUSD narxi: {xauusd['Last Trade']}): "))
        pair = input("Qaysi platformada ishlayapsiz ? (Misol uchun: EURUSD, USDJPY, XAUUSD, BTCUSD): ").upper()
        lot_size = float(input("Necha lotda (e.g., 0.1, 1.0): "))
        
        # Calculate the pips
        pips = calculate_pips(entry, exit, pair)
        print(f"Pips: {pips} pips")

        # Calculate the pip value
        pip_value = calculate_pip_value(pips, lot_size, pair)
        print(f"Foida: ${pip_value}")
    except ValueError:
        print("Malumotlar xato berilgan")

if __name__ == "__main__":
    main()
