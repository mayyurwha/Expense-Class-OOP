from alt_sch_exam import Expense, ExpenseDatabase

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
