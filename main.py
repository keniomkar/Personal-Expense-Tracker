from user import register, login
from account import create_account, view_accounts
from transaction import add_transaction
from budget import set_budget
from report import generate_report

def main():
    print("=== Personal Expense Tracker ===")
    choice = input("1. Register\n2. Login\nChoose: ")

    if choice == '1':
        register()
        user_id = login()
    elif choice == '2':
        user_id = login()
    else:
        print("Invalid choice")
        return

    if not user_id:
        return

    while True:
        print("\n--- Menu ---")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Add Transaction")
        print("4. Set Budget")
        print("5. Generate Report")
        print("6. Exit")
        option = input("Choose: ")

        if option == '1':
            create_account(user_id)
        elif option == '2':
            view_accounts(user_id)
        elif option == '3':
            view_accounts(user_id)
            acc_id = int(input("Enter Account ID to add transaction: "))
            add_transaction(acc_id)
        elif option == '4':
            set_budget(user_id)
        elif option == '5':
            generate_report(user_id)
        elif option == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
