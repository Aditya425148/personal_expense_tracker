import json

# File to store expenses
EXPENSE_FILE = 'expenses.json'

# Load data from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    description = input("Enter description: ")
    category = input("Enter category (e.g., Food, Travel, Entertainment): ")
    amount = float(input("Enter amount: "))
    
    expense = {
        'description': description,
        'category': category,
        'amount': amount
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return
    
    print("\nExpenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['description']} - {expense['category']} - ₹{expense['amount']}")
    print()

# Remove an expense
def remove_expense(expenses):
    if not expenses:
        print("No expenses to remove.")
        return
    
    view_expenses(expenses)
    
    try:
        expense_num = int(input("Enter the expense number to remove: "))
        
        if 1 <= expense_num <= len(expenses):
            removed_expense = expenses.pop(expense_num - 1)
            save_expenses(expenses)
            print(f"Expense '{removed_expense['description']}' removed successfully!")
        else:
            print("Invalid expense number.")
    except ValueError:
        print("Please enter a valid number.")

# Get summary of expenses by category
def expense_summary(expenses):
    if not expenses:
        print("No expenses to summarize.")
        return
    
    summary = {}
    for expense in expenses:
        category = expense['category']
        summary[category] = summary.get(category, 0) + expense['amount']
    
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category}: ₹{total}")
    print()

# Main menu
def menu():
    expenses = load_expenses()

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Remove Expense")  # New option to remove expenses
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            expense_summary(expenses)
        elif choice == '4':
            remove_expense(expenses)
        elif choice == '5':
            print("Thank You")
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    menu()
