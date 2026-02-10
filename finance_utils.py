# finance_utils.py
# Custom module containing helper functions for validation, formatting, and file output

import os


def validate_positive_number(value):
    """
    Validate that a number is greater than zero.
    Raises a ValueError if the condition is not met.

    """
    if value <= 0:
        raise ValueError("Value must be greater than zero")
    return value


def format_currency(amount):
    """
    Format a numeric value as currency for display purposes.

    """
    return f"${amount:.2f}"


def save_to_file(user):
    """
    Save the user's financial data to a text file.
    Includes error handling for file operations.

    """
    try:
        # Create a file path in the same directory as this module
        file_path = os.path.join(os.path.dirname(__file__), "finance_data.txt")

        # Open the file in write mode
        with open(file_path, "a") as file:
            # Write user and budget information
            file.write(f"Name: {user.get_name()}\n")
            file.write(f"Budget Period: {user.period}\n")
            file.write(f"Income: {format_currency(user.income)}\n")

            # Write expense details
            file.write("Expenses:\n")
            for name, amount in user.expenses.items():
                file.write(f"  {name}: {format_currency(amount)}\n")

            # Write the calculated totals
            file.write(
                f"Total Expenses: {format_currency(user.total_expenses())}\n")
            file.write(
                f"Remaining Budget: {format_currency(user.remaining_budget())}\n")
            file.write(f"Savings Goal: {format_currency(user.savings_goal)}\n")

    except IOError:
        # Handles file input/output errors
        print("Error: Unable to write data to file.")
