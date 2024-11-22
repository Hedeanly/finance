import tkinter as tk
from tkinter import messagebox


# Create the main application window
class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x400")

        # List to store expenses
        self.expenses = []

        # UI Elements
        self.label = tk.Label(self.root, text="Expense Tracker", font=("Arial", 20))
        self.label.pack(pady=10)

        self.expense_name_label = tk.Label(self.root, text="Expense Name")
        self.expense_name_label.pack(pady=5)

        self.expense_name_entry = tk.Entry(self.root)
        self.expense_name_entry.pack(pady=5)

        self.expense_amount_label = tk.Label(self.root, text="Expense Amount")
        self.expense_amount_label.pack(pady=5)

        self.expense_amount_entry = tk.Entry(self.root)
        self.expense_amount_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Expenses", command=self.view_expenses)
        self.view_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Expense", command=self.delete_expense)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear Fields", command=self.clear_fields)
        self.clear_button.pack(pady=5)

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(pady=10, expand=True, fill=tk.BOTH)

    def add_expense(self):
        name = self.expense_name_entry.get()
        amount = self.expense_amount_entry.get()

        if not name or not amount:
            messagebox.showerror("Input Error", "Both fields are required.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a number.")
            return

        self.expenses.append((name, amount))
        self.clear_fields()
        messagebox.showinfo("Success", "Expense added successfully!,hi")

    def view_expenses(self):
        self.listbox.delete(0, tk.END)
        for expense in self.expenses:
            self.listbox.insert(tk.END, f"{expense[0]}: ${expense[1]:.2f}")

    def delete_expense(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.expenses[index]
            self.view_expenses()
            messagebox.showinfo("Success", "Expense deleted successfully!")
        else:
            messagebox.showerror("Selection Error", "Please select an expense to delete.")

    def clear_fields(self):
        self.expense_name_entry.delete(0, tk.END)
        self.expense_amount_entry.delete(0, tk.END)


# Main loop to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
