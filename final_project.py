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
"""

# Constant message for invalid input
MSG_INVALID_VALUE = "You cannot enter zero or a negative value."


def request_positive_amount(message):
    """
    Request a positive amount from the user.

    Args:
        message (str): Message displayed to the user.

    Returns:
        float: A positive value entered by the user.
    """
    while True:
        value = float(input(message))

        if value <= 0:
            print(MSG_INVALID_VALUE)
        else:
            return value


def separator(num_chars):
    """
    Print a horizontal separator line using '=' characters.

    Args:
        num_chars (int): Number of '=' characters to print.
    """
    print("=" * num_chars)


def main():
    # List of available denominations in descending order
    denominations = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 2, 1] # You can add bills and/or coins if needed

    # Number of characters used for the separator line
    num_chars = 52

    # Display program title
    separator(num_chars)
    print("\tPurchase SIMULATOR with Exact Change")
    separator(num_chars)
    print()

    # Request purchase amount
    total_amount = request_positive_amount("Enter the total amount of the purchase: ")

    print()

    # Request payment amount
    payment_amount = request_positive_amount("Enter the amount paid by the customer: ")

    # Check if payment is sufficient
    if payment_amount < total_amount:
        print("\nInsufficient payment. You are short by:", int(total_amount - payment_amount))

    else:
        # Calculate change
        change = int(payment_amount - total_amount)

        # Show total change
        print("\nTotal change to return:", change)

        if change > 0:

            # Dictionary to store denominations and quantities
            change_to_give = {}

            # Calculate exact change
            for denom in denominations:

                if change >= denom:

                    quantity = change // denom

                    change -= quantity * denom

                    change_to_give[denom] = quantity

            # Display breakdown
            print("\nGive the customer:")

            for denom, quantity in change_to_give.items():
                print(f"{quantity} bill(s)/coin(s) of {denom}")

        else:
            print("No change is due.")

        print("\nThank you very much for your purchase.")


if __name__ == "__main__":
    main()
