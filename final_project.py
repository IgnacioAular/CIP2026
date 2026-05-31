"""
Purchase Simulator with Exact Change

This program simulates a purchase and calculates the exact change
to give back using available denominations (bills and coins).

The user inputs:
- total_amount: the total cost of the purchase
- payment_amount: the amount of money given by the customer

The program outputs:
- The total change to return
- A breakdown of how many of each denomination to give

GitHub URL:
- https://github.com/IgnacioAular/CIP2026/blob/main/final_project.py
"""

# Constant message for invalid input
MSG_INVALID_VALUE = "You cannot enter zero or a negative value."

# Available denominations in descending order
DENOMINATIONS = [
    100000, 50000, 20000, 10000, 5000, 2000,
    1000, 500, 200, 100, 50, 25, 10, 5, 2, 1
]

# Number of characters used for separator lines
SEPARATOR_LENGTH = 52


def request_positive_amount(message):
    """
    Request a positive amount from the user, handling invalid input.

    Args:
        message (str): Message displayed to the user.

    Returns:
        float: A positive numeric value entered by the user.
    """
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print(MSG_INVALID_VALUE)
            else:
                return value

        except ValueError:
            print("Please enter a valid numeric value.")


def separator(num_chars):
    """
    Print a horizontal separator line.

    Args:
        num_chars (int): Number of '=' characters.
    """
    print("=" * num_chars)


def display_title():
    """Display the program title."""
    separator(SEPARATOR_LENGTH)
    print("\tPurchase SIMULATOR with Exact Change")
    separator(SEPARATOR_LENGTH)
    print()


def calculate_change(change_amount):
    """
    Calculate the exact change using available denominations.

    Args:
        change_amount (int): Amount of change to return.

    Returns:
        dict: Denomination as key and quantity as value.
    """
    change_to_give = {}

    for denomination in DENOMINATIONS:
        if change_amount >= denomination:
            quantity = change_amount // denomination
            change_amount -= quantity * denomination
            change_to_give[denomination] = quantity

    return change_to_give


def display_change(change_to_give):
    """
    Display the denomination breakdown.

    Args:
        change_to_give (dict): Dictionary containing denomination counts.
    """
    print("\nGive the customer:")

    for denomination, quantity in change_to_give.items():
        print(f"{quantity} bill(s)/coin(s) of {denomination}")


def main():
    """Run the purchase simulation."""

    display_title()

    total_amount = request_positive_amount(
        "Enter the total amount of the purchase: "
    )

    print()

    payment_amount = request_positive_amount(
        "Enter the amount paid by the customer: "
    )

    if payment_amount < total_amount:
        shortage = int(total_amount - payment_amount)
        print(f"\nInsufficient payment. You are short by: {shortage}")
        return

    change = int(payment_amount - total_amount)

    print(f"\nTotal change to return: {change}")

    if change > 0:
        change_to_give = calculate_change(change)
        display_change(change_to_give)
    else:
        print("No change is due.")

    print("\nThank you very much for your purchase.")


if __name__ == "__main__":
    main()
