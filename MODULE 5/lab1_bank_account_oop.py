# MODULE 5 - LAB 1: Bank Account System using OOP

class BankAccount:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"Rs. {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print("\n===== ACCOUNT DETAILS =====")
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print(f"Available Balance: Rs. {self.balance:.2f}")


def main():
    print("===== BANK ACCOUNT SYSTEM =====")
    holder = input("Enter account holder name: ").strip()
    number = input("Enter account number: ").strip()

    try:
        opening_balance = float(input("Enter opening balance: "))
        if opening_balance < 0:
            print("Opening balance cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    account = BankAccount(holder, number, opening_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                account.deposit(float(input("Enter deposit amount: Rs. ")))
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == "2":
            try:
                account.withdraw(float(input("Enter withdrawal amount: Rs. ")))
            except ValueError:
                print("Please enter a valid amount.")
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Thank you for using the Bank Account System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
