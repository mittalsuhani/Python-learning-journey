# project 10 is an expense tracker
#it uses concepts of file handling and date time processing
import  json # importing json module to handle file operations

# importing datetime module to handle date operations
import datetime  

# Function to load expenses from a file
def load_expenses(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# to save expenses to a file
def save_expenses(filename, expenses):
    with open(filename, 'w') as file:
        json.dump(expenses, file)

# to add a new expense
def add_expense(expenses, amount, category, date):
    expense = {
        'amount': amount,
        'category': category,
        'date': date
    }
    expenses.append(expense)

# to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"{expense['date']}: ${expense['amount']:.2f} - {expense['category']}")

def main(): 
    filename = 'expenses.json'
    expenses = load_expenses(filename)  # list which will store all expenses

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
                if not date_str:
                    date_str = datetime.now().strftime('%Y-%m-%d')
                else:
                    datetime.strptime(date_str, '%Y-%m-%d')  # Validate date format
                add_expense(expenses, amount, category, date_str)   # adding expense to the list    
                save_expenses(filename, expenses)                   # saving expenses to the file
                print("Expense added successfully.")
            except ValueError:
                print("Invalid input, please try again.")
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

main()
