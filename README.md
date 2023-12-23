# Expense-Class-OOP
The goal of this task is to implement two classes, Expense and ExpenseDatabase to model and manage financial expenses.

PROJECT DESCRIPTION
The python script attached implements an expense tracking system using two classes namely: Expense and ExpenseDatabase. The classes are designed in such a way to model individual financial expenses and manage a collection of expenses, respectively.

Overview of the core elements of the code:

Expense Class:
Attributes:

id: A unique identifier generated as a UUID string.
title: A string representing the title of the expense.
amount: A float representing the amount of the expense.
created_at: A timestamp indicating when the expense was created (in UTC).
updated_at: A timestamp indicating the last time the expense was updated (in UTC).


Methods:
__init__: Initializes the attributes with provided values or default values.
update: Allows updating the title and/or amount of the expense. The updated_at attribute is automatically set to the current UTC timestamp whenever an update occurs.
to_dict: Returns a dictionary representation of the expense.


ExpenseDatabase Class:
Attributes:

expenses: A list storing instances of the Expense class.

Methods:
__init__: Initializes the expenses list.
add_expense: Adds an expense to the database.
remove_expense: Removes an expense from the database based on the expense ID.
get_expense_by_id: Retrieves an expense from the database by ID.
get_expense_by_title: Retrieves expenses from the database with a specific title (returns a list).
to_dict: Returns a list of dictionaries representing each expense in the database.

Implementation: The Test_alt_sch.py file is used to check the functionality of the alt_sch_exam script with the below steps:
Creates an instance of ExpenseDatabase.
Adds two expenses ("Groceries" and "Rent") to the database.
Updates the amount of the "Groceries" expense.
Retrieves expenses with the title "Groceries."
Removes the "Rent" expense from the database.
Prints the database as a list of dictionaries.



CLONE DECSRIPTION:
Open the GIT Bash Terminal
Navigate to the directory the project is to be clone using: git clone [repository name]

RUNNING THE CODE
Open the GIT Bash Terminal
Navigate to the project directory using: cd [project directory]
run the code using python3 [alt_sch_exam.py]
