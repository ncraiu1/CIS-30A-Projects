# models.py
# This file contains the class definitions used by the finance tracker program


class Person:
    """
    Base class representing a person.
    Stores basic identity information.

    """

    def __init__(self, name):
        # Store the person's name
        self.name = name

    def get_name(self):
        # Return the person's name
        return self.name


class User(Person):
    """
    Subclass of Person that represents a user of the finance tracker.
    Stores financial information and provides calculation methods.

    """

    def __init__(self, name):
        # Call the parent class constructor
        super().__init__(name)

        # Budget period (weekly or monthly)
        self.period = ""

        # Total income amount
        self.income = 0.0

        # Dictionary to store expenses
        self.expenses = {}

        # User-defined savings goal
        self.savings_goal = 0.0

    def add_income(self, amount):
        # Set or update the user's income
        self.income = amount

    def add_expense(self, name, amount):
        # Add a new expense or overwrite an existing one
        self.expenses[name] = amount

    def update_expense(self, name, amount):
        # Update an existing expense
        self.expenses[name] = amount

    def delete_expense(self, name):
        """
        Remove an expense from the expense dictionary.

        """
        if name in self.expenses:
            del self.expenses[name]
            return True
        return False

    def total_expenses(self):
        # Calculate and return the sum of all expenses
        return sum(self.expenses.values())

    def remaining_budget(self):
        # Calculates remaining budget after expenses
        return self.income - self.total_expenses()


class FinanceReport:
    """
    Handles displaying and generating financial summaries.

    """

    def __init__(self, user):
        # Stores a reference to the User object
        self.user = user

    def generate_summary(self):
        """
        Generate a formatted financial summary string.
        """
        summary = []
        summary.append(f"Name: {self.user.get_name()}")
        summary.append(f"Budget Period: {self.user.period}")
        summary.append(f"Income: ${self.user.income:.2f}")
        summary.append("Expenses:")

        for name, amount in self.user.expenses.items():
            summary.append(f"  {name}: ${amount:.2f}")

        summary.append(f"Total Expenses: ${self.user.total_expenses():.2f}")
        summary.append(
            f"Remaining Budget: ${self.user.remaining_budget():.2f}")
        summary.append(f"Savings Goal: ${self.user.savings_goal:.2f}")

        return "\n".join(summary)
