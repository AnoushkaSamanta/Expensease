from db_handler import create_db, add_expense, get_expenses, delete_expense,get_expenses_by_date,edit_expense
from visualization import plot_expenses_detailed_pie_chart,plot_expenses_bar_chart,plot_expenses_over_time
from datetime import datetime
from collections import defaultdict 
import csv

# Initialize database
create_db()

def add_expense_prompt():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category (e.g., Food, Travel, Utilities): ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    add_expense(description, amount, category, date)
    print("Expense added successfully.")
def view_expenses():
    expenses = get_expenses()
    print("\n{:<5} {:<20} {:<10} {:<15} {:<12}".format("ID", "Description", "Amount", "Category", "Date"))
    print("-" * 70)
    for expense in expenses:
        print("{:<5} {:<20} {:<10.2f} {:<15} {:<12}".format(expense[0], expense[1], expense[2], expense[3], expense[4]))
    print("-" * 70)


def delete_expense_prompt():
    expense_id = int(input("Enter the ID of the expense to delete: "))
    delete_expense(expense_id)
    print("Expense deleted successfully.")

def edit_expense_prompt():
    expense_id = int(input("Enter the ID of the expense to edit: "))
    description = input("Enter new description (or press Enter to skip): ")
    amount = input("Enter new amount (or press Enter to skip): ")
    amount = float(amount) if amount else None
    category = input("Enter new category (or press Enter to skip): ")
    date = input("Enter new date (YYYY-MM-DD) or press Enter to skip: ")
    edit_expense(expense_id, description, amount, category, date)
    print("Expense updated successfully.")

def export_to_csv(filename='expenses.csv'):
    expenses = get_expenses()
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Description', 'Amount', 'Category', 'Date'])
        writer.writerows(expenses)
    print(f"Expenses exported to {filename}.")

def filter_expenses_by_date_prompt():
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    expenses = get_expenses_by_date(start_date, end_date)
    
    print("\nFiltered Expenses:")
    print("ID\tDescription\tAmount\tCategory\tDate")
    print("-" * 50)
    if not expenses:
        print("No expenses found in this date range.")
    else:
        for expense in expenses:
            print(f"{expense[0]}\t{expense[1]}\t{expense[2]:.2f}\t{expense[3]}\t{expense[4]}")
    print("-" * 50)

def calculate_daily_expenses():
    expenses = get_expenses()
    daily_expenses = defaultdict(float)

    for expense in expenses:
        date = expense[4]  # Assuming the date is at index 4
        daily_expenses[date] += expense[2]  # Adding the amount to the respective date

    print("\nDaily Expenses:")
    print("Date\t\tTotal Amount")
    print("-" * 30)
    for date, total in daily_expenses.items():
        print(f"{date}\t{total:.2f}")
    print("-" * 30)

def calculate_monthly_expenses():
    expenses = get_expenses()
    monthly_expenses = defaultdict(float)

    for expense in expenses:
        date = expense[4]  # Assuming the date is at index 4
        month_year = date[:7]  # Extracting the year and month (YYYY-MM)
        monthly_expenses[month_year] += expense[2]  # Adding the amount to the respective month

    print("\nMonthly Expenses:")
    print("Month-Year\tTotal Amount")
    print("-" * 30)
    for month_year, total in monthly_expenses.items():
        print(f"{month_year}\t{total:.2f}")
    print("-" * 30)

# Add this function in expense_tracker.py

def set_monthly_budget():
    budget = float(input("Enter your monthly budget: "))
    with open('budget.txt', 'w') as f:
        f.write(str(budget))
    print("Monthly budget set successfully.")

# Add this function in expense_tracker.py

def set_monthly_budget():
    budget = float(input("Enter your monthly budget: "))
    with open('budget.txt', 'w') as f:
        f.write(str(budget))
    print("Monthly budget set successfully.")

def edit_monthly_budget():
    try:
        with open('budget.txt', 'r') as f:
            current_budget = float(f.read())
            print(f"Current Monthly Budget: {current_budget:.2f}")
            new_budget = float(input("Enter your new monthly budget: "))
            with open('budget.txt', 'w') as f:
                f.write(str(new_budget))
            print("Monthly budget updated successfully.")
    except FileNotFoundError:
        print("No budget set. Please set a budget first.")

def check_budget():
    try:
        with open('budget.txt', 'r') as f:
            budget = float(f.read())
            expenses = get_expenses()
            total_expenses = sum(expense[2] for expense in expenses)  # Sum amounts
            remaining_budget = budget - total_expenses
            
            print(f"Monthly Budget: {budget:.2f}")
            print(f"Total Expenses: {total_expenses:.2f}")
            print(f"Remaining Budget: {remaining_budget:.2f}")
            if remaining_budget < 0:
                print("Warning: You have exceeded your budget!")
    except FileNotFoundError:
        print("No budget set. Please set a budget first.")


# Modify the main function to include budget options
def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Set Monthly Budget")
        print("5. Edit Monthly Budget")
        print("6. Check Budget")
        print("7. Filter Expenses by Date")
        print("8. Export Expenses to CSV")
        print("9. View Daily Expenses")
        print("10. View Monthly Expenses")
        print("11. View Expense Summary (Pie Chart)")
        print("12. Plot bar graph")
        print("13. Plot overtime expenses")
        print("14. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense_prompt()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense_prompt()
        elif choice == '4':
            set_monthly_budget()
        elif choice == '5':
            edit_monthly_budget()
        elif choice == '6':
            check_budget()
        elif choice == '7':
            filter_expenses_by_date_prompt()
        elif choice == '8':
            export_to_csv()
        elif choice == '9':
            calculate_daily_expenses()
        elif choice == '10':
            calculate_monthly_expenses()
        elif choice == '11':
            plot_expenses_detailed_pie_chart()
            continue
        elif choice=='12':
            plot_expenses_bar_chart() 
            continue
        elif choice=='13':
            plot_expenses_over_time() 
            continue     
        elif choice == '14':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")






if __name__ == "__main__":
    main()
