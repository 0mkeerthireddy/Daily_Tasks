
# ATM Banking System

## Project Overview
The ATM Banking System is a simple Python-based console application that simulates basic ATM operations. It allows users to enter their initial balance and perform banking transactions through a menu-driven program.

## Technologies Used
- Python
- While Loop
- If-Else Conditions
- Lists
- User Input and Output
- Type Conversion

## Features
1. **Enter Initial Balance** – User can enter their starting account balance.
2. **Check Balance** – Displays the available balance.
3. **Deposit Money** – Allows users to deposit money and updates the balance.
4. **Withdraw Money** – Allows users to withdraw money if sufficient balance is available.
5. **Transaction History** – Displays all deposit and withdrawal transactions.
6. **Input Validation** – Rejects zero and negative transaction amounts.
7. **Invalid Choice Handling** – Displays an error message for invalid menu options.
8. **Exit** – Allows users to exit the application.

## Project Structure

```text
ATM-Banking-System/
│
├── atm_banking_system.py
└── README.md
```

## How to Run the Project

### Step 1: Install Python
Make sure Python is installed on your system.

### Step 2: Open the Project
Open the project folder in VS Code.

### Step 3: Run the Program
Open the terminal and execute:

```bash
python atm_banking_system.py
```

## Sample Output

```text
Enter your initial balance: 15000

===== ATM MENU =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit

Enter your choice: 1
Available Balance: 15000

Enter your choice: 2
Enter deposit amount: 2000
Deposit successful!
Updated Balance: 17000

Enter your choice: 3
Enter withdrawal amount: 5000
Withdrawal successful!
Updated Balance: 12000

Enter your choice: 5
Thank you for using ATM!
```

## Python Concepts Practiced

- Variables and Data Types
- User Input (`input()`)
- Type Conversion (`float()`)
- While Loop
- If, Elif and Else
- Lists
- List `append()` Method
- `len()` Function
- For Loop
- Break Statement
- Conditional Statements

## Learning Outcome

Through this project, I learned how to use Python loops, conditions, lists, and user input to develop a simple real-world banking application. I also practised balance calculations, transaction management, and input validation.

## Future Enhancements

- Add PIN verification.
- Handle invalid numeric inputs using `try-except`.
- Store transaction details in a file or database.
- Add account number verification.
- Display date and time for each transaction.

---

**Project:** ATM Banking System  
**Language:** Python  
**Type:** Console-Based Application
