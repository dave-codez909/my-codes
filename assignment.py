import tkinter as tk
from tkinter import messagebox

class Wallet:
    def __init__(self):
        self.balances = {}

    def add_money(self, currency, amount):
        if currency in self.balances:
            self.balances[currency] += amount
        else:
            self.balances[currency] = amount

    def spend_money(self, currency, amount):
        if currency in self.balances and self.balances[currency] >= amount:
            self.balances[currency] -= amount
        else:
            raise ValueError("Insufficient funds or currency not found")

    def check_balance(self, currency):
        return self.balances.get(currency, 0)

class WalletApp:
    def __init__(self, root):
        self.wallet = Wallet()
        
        self.root = root
        self.root.title("Wallet Application")

        self.currency_label = tk.Label(root, text="Currency:")
        self.currency_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.currency_entry = tk.Entry(root)
        self.currency_entry.grid(row=0, column=1, padx=10, pady=10)

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Money", command=self.add_money)
        self.add_button.grid(row=2, column=0, padx=10, pady=10)
        
        self.spend_button = tk.Button(root, text="Spend Money", command=self.spend_money)
        self.spend_button.grid(row=2, column=1, padx=10, pady=10)
        
        self.balance_button = tk.Button(root, text="Check Balance", command=self.check_balance)
        self.balance_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.output_label = tk.Label(root, text="")
        self.output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def add_money(self):
        currency = self.currency_entry.get().strip()
        amount = self.amount_entry.get().strip()
        if currency and amount:
            try:
                amount = float(amount)
                self.wallet.add_money(currency, amount)
                self.output_label.configure(text=f"Added {amount} {currency}.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        else:
            messagebox.showerror("Invalid Input", "Please enter both currency and amount.")

    def spend_money(self):
        currency = self.currency_entry.get().strip()
        amount = self.amount_entry.get().strip()
        if currency and amount:
            try:
                amount = float(amount)
                self.wallet.spend_money(currency, amount)
                self.output_label.configure(text=f"Spent {amount} {currency}.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid amount.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Invalid Input", "Please enter both currency and amount.")

    def check_balance(self):
        currency = self.currency_entry.get().strip()
        if currency:
            balance = self.wallet.check_balance(currency)
            self.output_label.configure(text=f"Balance for {currency}: {balance}")
        else:
            messagebox.showerror("Invalid Input", "Please enter a currency.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WalletApp(root)
    root.mainloop()
