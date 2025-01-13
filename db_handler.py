import sqlite3
import csv
def create_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(description, amount, category, date):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (description, amount, category, date)
        VALUES (?, ?, ?, ?)
    ''', (description, amount, category, date))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()
    conn.close()
    return expenses

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()

def edit_expense(expense_id, description=None, amount=None, category=None, date=None):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    
    # Update only the fields that have been provided
    if description:
        cursor.execute('UPDATE expenses SET description = ? WHERE id = ?', (description, expense_id))
    if amount:
        cursor.execute('UPDATE expenses SET amount = ? WHERE id = ?', (amount, expense_id))
    if category:
        cursor.execute('UPDATE expenses SET category = ? WHERE id = ?', (category, expense_id))
    if date:
        cursor.execute('UPDATE expenses SET date = ? WHERE id = ?', (date, expense_id))
    
    conn.commit()
    conn.close()

def get_expenses_by_date(start_date, end_date):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses WHERE date BETWEEN ? AND ?', (start_date, end_date))
    expenses = cursor.fetchall()
    conn.close()
    return expenses
