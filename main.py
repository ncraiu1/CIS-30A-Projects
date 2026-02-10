# main.py
# Main entry point for the Personal Finance Tracking Program

from models import User
from models import FinanceReport
from finance_utils import validate_positive_number, format_currency, save_to_file


def display_menu():
    """
    Display the main menu options to the user.

    """
    print("\n$$$ Personal Finance Tracker $$$")
    print("1. Set Budget Period and Savings Goal")
    print("2. Add / Update Income")
    print("3. Add / Update Expense")
    print("4. View Financial Report")
    print("5. Delete Expense")
    print("6. Save Data to File")
    print("7. Exit")


def view_summary(user):
    """
    Display a financial summary using the FinanceReport class.

    """
    report = FinanceReport(user)
    print("\n--- Financial Summary ---")
    print(report.generate_summary())


def set_budget(user):
    """
    Prompt the user to set the budget period and savings goal.
    Includes input validation and looping until valid input is provided.

    """
    # Loop until a valid budget period is entered
    while True:
        period = input("Enter budget period (weekly/monthly): ").lower()
        if period in ["weekly", "monthly"]:
            user.period = period
            break
        else:
            print("Invalid period. Please enter 'weekly' or 'monthly'.")

    # Loop until a valid savings goal is entered
    while True:
        try:
            goal = float(input("Enter savings goal: "))
            user.savings_goal = validate_positive_number(goal)
            break
        except ValueError:
            print("Invalid savings goal. Please enter a positive number.")


def set_income(user):
    """
    Prompt the user to enter or update income.
    Uses exception handling for invalid numeric input.

    """
    while True:
        try:
            income = float(input("Enter income amount: "))
            user.add_income(validate_positive_number(income))
            break
        except ValueError:
            print("Invalid income amount. Please enter a positive number.")


def set_expense(user):
    """
    Prompt the user to add or update an expense.
    Stores expense data in a dictionary.

    """
    expense_name = input("Enter expense name: ")

    while True:
        try:
            amount = float(input("Enter expense amount: "))
            amount = validate_positive_number(amount)
            user.add_expense(expense_name, amount)
            break
        except ValueError:
            print("Invalid expense amount. Please enter a positive number.")


def delete_expense(user):
    """
    Allow the user to delete an existing expense.

    """
    if not user.expenses:
        print("No expenses to delete.")
        return

    print("\nCurrent Expenses:")
    for name in user.expenses:
        print(f"- {name}")

    expense_name = input("Enter the name of the expense to delete: ")

    if user.delete_expense(expense_name):
        print(f"Expense '{expense_name}' deleted successfully.")
    else:
        print("Expense not found.")


def view_summary(user):
    """
    Display a summary of the user's financial information.
    Demonstrates iteration and decision-making.

    """
    print("\n--- Financial Summary ---")
    print(f"Income: {format_currency(user.income)}")

    # Calculate total expenses using iteration
    total = 0
    for amount in user.expenses.values():
        total += amount

    print(f"Total Expenses: {format_currency(total)}")

    # Decision making based on remaining budget
    if user.remaining_budget() >= 0:
        print(f"Remaining Budget: {format_currency(user.remaining_budget())}")
    else:
        print("Warning: You are over budget!")

    print(f"Savings Goal: {format_currency(user.savings_goal)}")


def main():
    """
    Main program execution function.
    Controls program flow using a loop and conditional branching.

    """
    # Prompt user for name and create User object
    name = input("Enter your name: ")
    user = User(name)

    running = True

    # Main menu loop
    while running:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            set_budget(user)
        elif choice == "2":
            set_income(user)
        elif choice == "3":
            set_expense(user)
        elif choice == "4":
            view_summary(user)
        elif choice == "5":
            delete_expense(user)
        elif choice == "6":
            save_to_file(user)
            print("Data saved successfully.")
        elif choice == "7":
            running = False
        else:
            print("Invalid menu choice.")


# Call the main function to start the program
main()
