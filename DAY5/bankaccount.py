class BankAccount:
    def __init__(self, accountNumber, balance=0):
        self.accountNumber = accountNumber
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.accountNumber}.")
        else:
            print("Invalid amount for deposit.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} from account {self.accountNumber}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount for withdrawal.")
    
    def get_balance(self):
        print(f"Current balance of account {self.accountNumber}: {self.balance}")

# Example usage:
account1 = BankAccount("123456")
account1.get_balance()  # Output: Current balance of account 123456: 0

account1.deposit(1000)  # Output: Deposited 1000 into account 123456.
account1.get_balance()  # Output: Current balance of account 123456: 1000

account1.withdraw(500)  # Output: Withdrew 500 from account 123456.
account1.get_balance()  # Output: Current balance of account 123456: 500

account1.withdraw(1000) # Output: Insufficient funds.
account1.get_balance()  # Output: Current balance of account 123456: 500

account1.deposit(-200)  # Output: Invalid amount for deposit.
