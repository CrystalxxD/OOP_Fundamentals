class BankAccount:
    def __init__(self, account_number, owner_name, initial_balance=0):
        if len(account_number) != 6:
            raise ValueError("Account number must be exactly 6 characters long")
        
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = initial_balance

    # Getter methods
    def get_account_number(self):
        return self.__account_number
    
    def get_owner_name(self):
        return self.__owner_name
    
    def get_balance(self):
        return self.__balance

    # Setter methods
    def set_owner_name(self, new_name):
        if not isinstance(new_name, str) or len(new_name.strip()) == 0:
            raise ValueError("Owner name must be a non-empty string")
        self.__owner_name = new_name.strip()

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds for withdrawal")
        self.__balance -= amount
        return self.__balance

    def __str__(self):
        return (f"Account Number: {self.__account_number}\n"
                f"Owner Name: {self.__owner_name}\n"
                f"Balance: ${self.__balance:.2f}")

# Extension Level 2: System admin function
def create_customer_account():
    print("\nCreating new customer account...")
    while True:
        account_number = input("Enter 6-digit account number: ")
        if len(account_number) == 6 and account_number.isdigit():
            break
        print("Account number must be exactly 6 digits")
    
    while True:
        owner_name = input("Enter owner's name: ").strip()
        if owner_name:
            break
        print("Owner name cannot be empty")
    
    while True:
        initial_balance = input("Enter initial balance (default 0): ").strip()
        if not initial_balance:
            initial_balance = 0
            break
        try:
            initial_balance = float(initial_balance)
            if initial_balance >= 0:
                break
            print("Balance cannot be negative")
        except ValueError:
            print("Please enter a valid number")
    
    return BankAccount(account_number, owner_name, initial_balance)