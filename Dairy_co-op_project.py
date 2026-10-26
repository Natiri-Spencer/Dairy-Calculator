"""
Dairy Co-op Payment Calculator
------------------------------

Calculates the amount payable to a farmer based on:

    Total Payment = Litres Supplied × Current Buying Price

The current buying price is read from price.txt.
If the file is not available or contains invalid data,
a default price is used.

Usage:
    python dairy_calculator.py
"""

DEFAULT_PRICE = 55.0  # KES per litre


def get_current_price():
    """
    Return the current milk buying price.

    Reads the value from price.txt.
    Falls back to DEFAULT_PRICE when the file
    is missing or contains invalid data.
    """
    try:
        with open("price.txt", "r", encoding="utf-8") as file:
            return float(file.read().strip())
    except (FileNotFoundError, ValueError):
        return DEFAULT_PRICE


def calculate_payment(litres, price_per_litre):
    """
    Calculate total payment owed.

    Args:
        litres (float): Quantity supplied.
        price_per_litre (float): Buying price.

    Returns:
        float: Total payment.
    """
    return litres * price_per_litre


def run():
    """Run the Dairy Co-op Payment Calculator."""

    price = get_current_price()

    print("\nKiambu Dairy Co-op Payment Calculator")
    print("-------------------------------------")
    print(f"Current buying price: KES {price:.2f} per litre\n")

    name = input("Farmer name: ").strip()

    if not name:
        print("Error: Farmer name is required.")
        return

    try:
        litres = float(input("Litres supplied today: "))

        if litres <= 0:
            print("Error: Litres must be greater than zero.")
            return

    except ValueError:
        print("Error: Please enter a valid number for litres.")
        return

    total = calculate_payment(litres, price)

    print("\nPayment Summary")
    print("----------------")
    print(f"Farmer : {name}")
    print(f"Litres : {litres:.2f}")
    print(f"Price  : KES {price:.2f}/litre")
    print(f"Total  : KES {total:,.2f}")


if __name__ == "__main__":
    run()