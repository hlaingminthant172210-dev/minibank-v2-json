# MiniBank System in Python

## Overview

MiniBank is a simple command-line banking application written in Python.

The program allows users to:
- Register a new account
- Log in with username and password
- Transfer money to another user
- Withdraw money
- Update username, password, and account balance

All user data is stored in a JSON file (`all_user_info.json`), so information remains available after the program is closed.

---

## Features

### User Registration
- Create a new account
- Username validation
- Password confirmation
- Minimum starting balance of 1000

### User Login
- Login using username and password

### Banking Operations
- Transfer money to another user
- Withdraw money
- Add funds to account
- Update username
- Update password

### Data Persistence
- All account information is stored in a JSON file

---

## File Structure

```text
MiniBank/
├── main.py
├── all_user_info.json
└── README.md
```

---

## Data Format

User information is stored in JSON format like this:

```json
{
    "1": {
        "name": "Alice",
        "password": "1234",
        "amount": 5000
    },
    "2": {
        "name": "Bob",
        "password": "5678",
        "amount": 3000
    }
}
```

---

## How the Program Works

### Registration
1. User enters a username.
2. Program checks whether the username already exists.
3. User enters and confirms a password.
4. User enters an initial deposit (minimum 1000).
5. Account information is saved to `all_user_info.json`.

### Login
1. User enters username and password.
2. Program verifies credentials.
3. If successful, the banking menu is displayed.

### Transfer Money
1. User enters the recipient username.
2. Program checks that the recipient exists.
3. User enters transfer amount.
4. Balance is deducted from sender and added to recipient.

### Withdraw Money
1. User enters withdrawal amount.
2. Program checks if sufficient balance exists.
3. Amount is deducted from the account.

### Update Information
User can:
- Change username
- Change password
- Add money to account

---

## Main Methods

### `register()`
Creates a new account and stores it in the JSON file.

### `login()`
Authenticates the user.

### `transferMoney()`
Transfers money between users.

### `withdrawMoney()`
Withdraws money from the current account.

### `updateInfo()`
Updates account information.

### `existUser()`
Checks login credentials.

### `exist_rUser()`
Checks whether a username already exists.

---

## Requirements

- Python 3.x

No external libraries are required.

---

## How to Run

```bash
python3 main.py
```

---

## Example Usage

```text
Press 1 to register
Press 2 to login
Press 3 to exit
```

After login:

```text
Press 1 to Transfer
Press 2 to Withdraw
Press 3 to Update
Press 4 to Exit
```

---

## Validation Rules

### Username
- Letters only (`A-Z`, `a-z`)
- Maximum 10 characters
- Must be unique

### Password
- Must match confirmation password

### Initial Amount
- Numbers only
- Minimum 1000

---

## Limitations

- Passwords are stored as plain text
- No deposit menu option after login
- No transaction history
- No account deletion

---

## Future Improvements

Possible enhancements:
- Password encryption
- Deposit function
- Transaction history
- Account deletion
- Better input validation
- Graphical User Interface (GUI)

---

## Concepts Used

- Object-Oriented Programming (Classes and Methods)
- JSON File Handling
- Exception Handling
- Input Validation
- Conditional Statements
- Loops

---

## Conclusion

This project is a beginner-friendly banking application that demonstrates how Python classes and JSON storage can be used to build a simple real-world system.
```