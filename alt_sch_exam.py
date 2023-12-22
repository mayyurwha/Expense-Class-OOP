from uuid import uuid4
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        self.title = title if title is not None else self.title
        self.amount = amount if amount is not None else self.amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

# Example usage:

# Create an ExpenseDatabase instance
expense_db = ExpenseDatabase()

# Add expenses to the database
expense1 = Expense("Groceries", 50.0)
expense2 = Expense("Rent", 1200.0)
expense_db.add_expense(expense1)
expense_db.add_expense(expense2)

# Update an expense
expense1.update(amount=60.0)

# Get expenses by title
grocery_expenses = expense_db.get_expense_by_title("Groceries")

# Remove an expense
expense_db.remove_expense(expense2.id)

# Print the database as a list of dictionaries
print(expense_db.to_dict())
