import tkinter as tk
from tkinter import messagebox

class BankingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking Credit and Deposit System")
        self.root.geometry("400x300")

        # Create frames
        self.frame1 = tk.Frame(self.root, bg="gray")
        self.frame1.pack(fill="x")

        self.frame2 = tk.Frame(self.root, bg="gray")
        self.frame2.pack(fill="x")

        self.frame3 = tk.Frame(self.root, bg="gray")
        self.frame3.pack(fill="x")

        # Create labels and entries
        self.label1 = tk.Label(self.frame1, text="Account Number:", bg="gray")
        self.label1.pack(side="left")

        self.entry1 = tk.Entry(self.frame1, width=20)
        self.entry1.pack(side="left")

        self.label2 = tk.Label(self.frame2, text="Amount:", bg="gray")
        self.label2.pack(side="left")

        self.entry2 = tk.Entry(self.frame2, width=20)
        self.entry2.pack(side="left")

        self.label3 = tk.Label(self.frame3, text="Transaction Type:", bg="gray")
        self.label3.pack(side="left")

        self.var = tk.StringVar()
        self.var.set("Credit")

        self.option1 = tk.Radiobutton(self.frame3, text="Credit", variable=self.var, value="Credit")
        self.option1.pack(side="left")

        self.option2 = tk.Radiobutton(self.frame3, text="Debit", variable=self.var, value="Debit")
        self.option2.pack(side="left")

        # Create buttons
        self.button1 = tk.Button(self.frame1, text="Submit", command=self.submit_transaction)
        self.button1.pack(side="right")

        self.button2 = tk.Button(self.frame2, text="Check Balance", command=self.check_balance)
        self.button2.pack(side="right")

        # Initialize account balance
        self.balance = 0

    def submit_transaction(self):
        account_number = self.entry1.get()
        amount = float(self.entry2.get())
        transaction_type = self.var.get()

        if transaction_type == "Credit":
            self.balance += amount
            messagebox.showinfo("Transaction Successful", f"Account {account_number} credited with ${amount:.2f}")
        elif transaction_type == "Debit":
            if amount > self.balance:
                messagebox.showerror("Insufficient Balance", "You do not have sufficient balance to debit")
            else:
                self.balance -= amount
                messagebox.showinfo("Transaction Successful", f"Account {account_number} debited with ${amount:.2f}")

        self.entry1.delete(0, "end")
        self.entry2.delete(0, "end")

    def check_balance(self):
        account_number = self.entry1.get()
        messagebox.showinfo("Account Balance", f"Account {account_number} balance is ${self.balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingSystem(root)
    root.mainloop()