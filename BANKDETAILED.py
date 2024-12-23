class BankAccount:
    def __init__(self, name, account_number):
        self.bank_name = "KOTAK BANK"
        self.name = name
        self.account_number = account_number
        self.balance = 0.0

    def display_details(self):
        print(f"Bank Details:")
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

# Example Usage
account_number = input("Enter your Account Number: ") 
account_holder = input("Enter your Name: ") 
account = BankAccount(account_holder, account_number)

while True:
    print("\nSelect an option:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.display_details()
    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == 3:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice.")





























































































        