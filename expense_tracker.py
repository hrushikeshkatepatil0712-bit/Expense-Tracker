



# import csv
# import os.path
#
# import os
# # with open('data.csv','r') as file:
# #     reader=csv.DictReader(file)
# #     for i in reader:
# #         print(i)
#
#
# data={'name':'shivani', 'age':25,'course':'python'}
# with open('data.csv','a',newline='') as file:
#     f = ['name', 'age', 'course']
#     writer=csv.DictWriter(file,fieldnames=f)
#
#     # if not os.path.exists('data.csv'):
#     #     writer.writeheader()
#
#     writer.writerow(data)
#
# print('the fil is saved')


#
# import csv
# from dataclasses import fields
#
# import tkinkter as tk
# from tkinter import messagebox
# import os
#
# # date, category, amount,note
#
#
# FILE_NAME='expenses.csv'
#
# expenses=[]
#
# def load_expenses():
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME,'r',newline='') as file:
#             reader=csv.DictReader(file)
#             if not 'date' or not 'category' or not 'amount':
#                 expenses.append(reader)
#
#
#
# def save_expenses_to_csv():
#     fileds=['date','category','amount','note']
#
#
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME,'a',newline='') as file:
#             writer=csv.DictWriter(file,fieldnames=fileds)
#             writer.writerow(expenses)
#
#     else:
#         with open(FILE_NAME,'a', newline='') as file:
#             writer=csv.DictWriter(file,fieldnames=fileds)
#             writer.writeheader()
#             writer.writerow(expenses)
#
# def add_expenses():
#     date=date_entry.get()
#     category=category.get()
#     amount=amount.get()
#     note=note.get()
#
#     if not date or not category or not amount:
#         messagebox.showwarning('all filled is required','please enter all data')
#         return
#     try:
#         float(amount)
#     except ValueError:
#         messagebox.showwarning('Error found', 'amount value showless int')
#
#
#     data_saver={
#         'date': date,
#         'category':category,
#         'amount':amount,
#         'note':note
#     }
#
# expenses.append(data_saver)
# save_expenses_to_csv(data_saver)
#
# date_entry.delete(0,tk.END)
# data_entry.delete(0,tk.END)
#
#
#
# load_expenses()
#
#
# root=tk.Tk()
# root.title('monthly expense tracker')




# TOTAL EXPENSE FEATURE ADD BUTTON


import csv
import os
import tkinter as tk
from tkinter import messagebox

FILENAME = "expenses.csv"
expenses = []

# Load expenses from file
def load_expense():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
        print("Loaded expenses:", expenses)

# Save a new expense to CSV
def save_expense_to_csv(expense):
    file_exist = os.path.exists(FILENAME)
    fields = ['date', 'category', 'amount', 'note']
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        if not file_exist:
            writer.writeheader()
        writer.writerow(expense)

# Add expense
def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    note = note_entry.get()

    if not date or not category or not amount:
        messagebox.showwarning("Missing Data", "Please fill all fields!")
        return

    try:
        float(amount)  # check amount is numeric
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number!")
        return

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'note': note
    }
    expenses.append(expense)
    save_expense_to_csv(expense)

    messagebox.showinfo("Success", "Expense added successfully!")

    # Clear fields
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

# View expenses
def view_expenses():
    view_win = tk.Toplevel(root)
    view_win.title("All Expenses")

    if not expenses:
        tk.Label(view_win, text="No expenses found!").pack(pady=10)
        return

    for exp in expenses:
        info = f"Date: {exp['date']} | Category: {exp['category']} | Amount: ₹{exp['amount']} | Note: {exp['note']}"
        tk.Label(view_win, text=info, anchor='w', justify='left').pack(fill='both', padx=10, pady=2)

# Show total expense
def show_total():
    try:
        total = sum(float(exp['amount']) for exp in expenses)
        messagebox.showinfo("Total Expense", f"Total Expense: ₹{total:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong while calculating total.\n{e}")

# GUI Start
load_expense()

root = tk.Tk()
root.title("Simple Expense Tracker")

# Headings and Entry Fields
tk.Label(root, text="Enter Date (YYYY-MM-DD):").pack(pady=2)
date_entry = tk.Entry(root, width=40)
date_entry.pack(pady=2)

tk.Label(root, text="Enter Category (e.g., Food, Travel):").pack(pady=2)
category_entry = tk.Entry(root, width=40)
category_entry.pack(pady=2)

tk.Label(root, text="Enter Amount:").pack(pady=2)
amount_entry = tk.Entry(root, width=40)
amount_entry.pack(pady=2)

tk.Label(root, text="Enter Note (optional):").pack(pady=2)
note_entry = tk.Entry(root, width=40)
note_entry.pack(pady=2)

# Buttons
tk.Button(root, text="Add Expense", command=add_expense, bg="lightgreen", width=30).pack(pady=5)
tk.Button(root, text="View All Expenses", command=view_expenses, bg="lightblue", width=30).pack(pady=5)
tk.Button(root, text="Show Total Expense", command=show_total, bg="lightyellow", width=30).pack(pady=5)

root.mainloop()
























