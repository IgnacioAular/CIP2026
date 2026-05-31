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

def main():
    # List of available denominations in descending order (bills first)
    denominations = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 2, 1]  # You can add bills and/or coins if needed

    # Number of characters used for the separator line
    num_chars = 52
    
    # Display program title
    separator(num_chars)
    print("\tPurchase SIMULATOR with Exact Change")
    separator(num_chars)
    print()
    
    # Ask user for the total cost of the purchase
    while True:
        total_amount = float(input("Enter the total amount of the purchase: "))
        if total_amount <= 0:
            print(MSG_INVALID_VALUE)
        else:
            break
    
    print()
    
    # Ask user for the payment amount
    while True:
        payment_amount = float(input("Enter the amount paid by the customer: "))
        if payment_amount <= 0:
            print(MSG_INVALID_VALUE)
        else:
            break

    # Check if the payment is enough
    if payment_amount < total_amount:
        print("\nInsufficient payment. You are short by:", int(total_amount - payment_amount))
    else:
        # Calculate the total change
        change = int(payment_amount - total_amount)  # Convert to integer for simplicity with bills
        
        # Show the total amount of change
        print("\nTotal change to return:", change)

        if change > 0:
            # Dictionary to store the number of each denomination to return
            change_to_give = {}

            # Loop through each denomination to calculate how many to give
            for denom in denominations:
                if change >= denom:
                    quantity = change // denom  # How many of this denomination to give
                    change -= quantity * denom  # Reduce the remaining change
                    change_to_give[denom] = quantity  # Store in dictionary

            # Display the breakdown of change
            print("\nGive the customer:")
            for denom, quantity in change_to_give.items():
                print(f"{quantity} bill(s)/coin(s) of {denom}")
        else:
            # No change needed
            print("No change is due.")
        
        # Farewell message
        print("\nThank you very much for your purchase.")


def separator(num_chars):
    """
    Print a horizontal separator line using '=' characters.

    Args:
        num_chars (int): Number of '=' characters to print.
    """
    print("=" * num_chars)


if __name__ == "__main__":
    main()
