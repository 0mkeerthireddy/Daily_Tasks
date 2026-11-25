
# ATM BANKING SYSTEM

# Initial account balance
balance = float(input("Enter your initial balance: "))

# Transaction history
transactions = []

while True:

    print("\n===== ATM BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # 1. Check Balance
    if choice == "1":
        print("Available Balance: Rs.", balance)

    # 2. Deposit Money
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            transactions.append(f"Deposited: Rs. {amount:.2f}")

            print("Money deposited successfully!")
            print("Updated Balance: Rs.", balance)

        else:
            print("Invalid amount! Deposit must be greater than zero.")

    # 3. Withdraw Money
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount! Withdrawal must be greater than zero.")

        elif amount <= balance:
            balance = balance - amount
            transactions.append(f"Withdrawn: Rs. {amount:.2f}")

            print("Please collect your cash.")
            print("Updated Balance: Rs.", balance)

        else:
            print("Insufficient balance!")

    # 4. Transaction History
    elif choice == "4":
        print("\n===== TRANSACTION HISTORY =====")

        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction)

    # 5. Exit
    elif choice == "5":
        print("Thank you for using our ATM!")
        break

    # Invalid Choice
    else:
        print("Invalid choice! Please select 1 to 5.")
