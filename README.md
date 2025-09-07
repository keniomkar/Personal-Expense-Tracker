# Personal Expense Tracker

## Project Overview
The Personal Expense Tracker is a command-line application built with Python and PostgreSQL that helps users manage their personal finances efficiently. Users can track income and expenses, manage multiple accounts, set budgets per category, and generate reports for better financial insights.

## Features
- User Management: Register and log in securely (multi-user support).
- Account Management: Create and manage multiple accounts such as Bank, Cash, or Wallet.
- Transaction Management: Add, update, and delete transactions with categories, descriptions, tags, and recurring options.
- Budget Management: Set budgets per category to track and control spending.
- Reporting: Generate summaries of expenses and account balances to monitor financial health.

## Tech Stack
- Backend: Python 3
- Database: PostgreSQL
- Libraries: psycopg2 for database connection, getpass for secure password input, datetime for date handling

## Project Structure
### personal_expense_tracker/  

| File           | Description                     |
|----------------|---------------------------------|
| main.py        | Main file (entry point)         |
| database.py    | PostgreSQL connection handling  |
| user.py        | User registration & login       |
| account.py     | Account creation & management   |
| transaction.py | Add, update, delete transactions|
| budget.py      | Budget creation & tracking      |
| report.py      | Generate expense reports        |         |
| README.md      | Project documentation           |

## Usage

- Register a new user or login with existing credentials.  
- Create one or more accounts.  
- Add transactions (income/expense) to your accounts.  
- Set budgets for categories.  
- Generate reports to view your spending and account balances.  

## Optional Enhancements
- Add delete/update transactions.  
- Add alerts for budget overspending.  
- Hash passwords using hashlib for security.  
