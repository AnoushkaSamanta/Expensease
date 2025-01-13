import matplotlib.pyplot as plt
from db_handler import get_expenses
from collections import defaultdict

def plot_expenses_detailed_pie_chart():
    expenses = get_expenses()
    
    # Calculate total amount per category
    category_totals = defaultdict(float)
    for expense in expenses:
        category = expense[3]
        amount = expense[2]
        category_totals[category] += amount
    
    # Extract categories and amounts for plotting
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())
    
    # Plot detailed pie chart
    plt.figure(figsize=(8, 6))
    wedges, texts, autotexts = plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    
    # Beautify the pie chart
    plt.setp(autotexts, size=10, weight="bold", color="white")
    plt.setp(texts, size=10, weight="bold")
    plt.title("Expense Summary by Category")
    plt.show()


def plot_expenses_bar_chart():
    expenses = get_expenses()
    
    # Calculate total amount per category
    category_totals = defaultdict(float)
    for expense in expenses:
        category = expense[3]
        amount = expense[2]
        category_totals[category] += amount
    
    # Extract categories and amounts for plotting
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())
    
    # Plot bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color='skyblue')
    plt.xlabel('Categories')
    plt.ylabel('Total Amount')
    plt.title('Total Expenses by Category')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_expenses_over_time():
    expenses = get_expenses()
    
    # Prepare data for plotting
    dates = defaultdict(float)
    for expense in expenses:
        date = expense[4]  # Get the date from the expense record
        amount = expense[2]
        dates[date] += amount
    
    # Sort dates
    sorted_dates = sorted(dates.keys())
    sorted_amounts = [dates[date] for date in sorted_dates]
    
    # Plot line graph
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_dates, sorted_amounts, marker='o', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Total Amount')
    plt.title('Expenses Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

