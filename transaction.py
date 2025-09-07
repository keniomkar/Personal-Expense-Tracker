from database import get_connection
from datetime import datetime

def add_transaction(account_id):
    conn = get_connection()
    cur = conn.cursor()
    
    amount = float(input("Enter amount (positive for income, negative for expense): "))
    category = input("Category (Food, Travel, Bills...): ")
    description = input("Description (optional): ")
    tags = input("Tags (optional): ")
    recurring = input("Recurring? (yes/no): ").lower() == 'yes'
    #recurring is a boolean it checks if the input is true or false
    date_str = input("Transaction date (YYYY-MM-DD) leave empty for today: ")
    # date_str stores date string like "2025-12-22"
    
    if not date_str:  #if no date in date_str that means its todays date
        transaction_date = datetime.today().date()
        #datetime.today is similar to datetime.date.today()
    else:
        transaction_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
    try:
        cur.execute(
            "INSERT INTO transactions (account_id, amount, category, description, tags, transaction_date, recurring) VALUES (%s, %s, %s, %s, %s, %s, %s)",(account_id, amount, category, description, tags, transaction_date, recurring)
        )
        #update account balance
        cur.execute(
            "UPDATE accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_id) 
        )
        conn.commit()
        print("Transaction added successfully")
    except Exception as e:
        print("Error: ",e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        