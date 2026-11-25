class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance       # Encapsulated balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful: ₹", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Transaction rejected: Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful: ₹", amount)

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print("Account Number :", self.account_number)
        print("Account Holder :", self.account_holder)
        print("Balance        : ₹", self.__balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added : ₹", interest)


# Create multiple account objects
account1 = BankAccount("BA101", "Amit", 50000)
account2 = SavingsAccount("SA102", "Neha", 75000, 5)
account3 = BankAccount("BA103", "Ravi", 40000)
account4 = SavingsAccount("SA104", "Priya", 60000, 4)

# Perform transactions
print("Account 1:")
account1.deposit(5000)
account1.withdraw(3000)
account1.display_details()

print("\nAccount 2:")
account2.deposit(5000)
account2.add_interest()
account2.display_details()

print("\nInvalid Transaction:")
account3.withdraw(50000)

# Store accounts in a list
accounts = [account1, account2, account3, account4]

# Sort accounts by balance using lambda
sorted_accounts = sorted(
    accounts,
    key=lambda account: account.get_balance()
)

print("\nAccounts Sorted by Balance:")
for account in sorted_accounts:
    print(
        account.account_number,
        "-",
        account.account_holder,
        "- ₹",
        account.get_balance()
    )

# Dictionary mapping account types to account numbers
account_types = {
    "BankAccount": set(),
    "SavingsAccount": set()
}

for account in accounts:
    if isinstance(account, SavingsAccount):
        account_types["SavingsAccount"].add(account.account_number)
    else:
        account_types["BankAccount"].add(account.account_number)

print("\nAccount Type Dictionary:")
print(account_types)