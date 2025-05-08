from bank_account import BankAccount, create_customer_account

def test_bank_account():
    # Test first account
    print("\nTesting Account 1:")
    try:
        acc1 = BankAccount("123456", "John Doe", 1000)
        print("\nAccount created successfully:")
        print(acc1)
        
        # Test getters
        print("\nTesting getters:")
        print("Account Number:", acc1.get_account_number())
        print("Owner Name:", acc1.get_owner_name())
        print("Balance:", acc1.get_balance())
        
        # Test deposit
        print("\nDepositing $200...")
        acc1.deposit(200)
        print("New balance:", acc1.get_balance())
        
        # Test withdraw
        print("\nWithdrawing $300...")
        acc1.withdraw(300)
        print("New balance:", acc1.get_balance())
        
        # Test setter
        print("\nChanging owner name to 'John Smith'...")
        acc1.set_owner_name("John Smith")
        print("New owner name:", acc1.get_owner_name())
        
        # Test invalid withdraw
        print("\nAttempting to withdraw $2000 (more than balance)...")
        try:
            acc1.withdraw(2000)
        except ValueError as e:
            print("Error:", e)
        
    except ValueError as e:
        print("Error creating account:", e)

    # Test second account
    print("\nTesting Account 2:")
    try:
        acc2 = BankAccount("789012", "Jane Smith", 500)
        print("\nAccount created successfully:")
        print(acc2)
        
        # Test getters
        print("\nTesting getters:")
        print("Account Number:", acc2.get_account_number())
        print("Owner Name:", acc2.get_owner_name())
        print("Balance:", acc2.get_balance())
        
        # Test deposit
        print("\nDepositing $100...")
        acc2.deposit(100)
        print("New balance:", acc2.get_balance())
        
        # Test withdraw
        print("\nWithdrawing $50...")
        acc2.withdraw(50)
        print("New balance:", acc2.get_balance())
        
        # Test invalid account number
        print("\nAttempting to create account with invalid number '12345'...")
        try:
            bad_acc = BankAccount("12345", "Error Case", 100)
        except ValueError as e:
            print("Error:", e)
        
    except ValueError as e:
        print("Error creating account:", e)

def test_admin_function():
    print("\nTesting system admin account creation:")
    account = create_customer_account()
    print("\nAccount created successfully:")
    print(account)
    
    # Test operations on admin-created account
    print("\nTesting operations on admin-created account:")
    print("Current balance:", account.get_balance())
    
    print("\nDepositing $150...")
    account.deposit(150)
    print("New balance:", account.get_balance())
    
    print("\nWithdrawing $75...")
    account.withdraw(75)
    print("New balance:", account.get_balance())

def main():
    print("Bank Account System Test\n")
    test_bank_account()
    test_admin_function()
    print("\nAll tests completed.")

if __name__ == "__main__":
    main()