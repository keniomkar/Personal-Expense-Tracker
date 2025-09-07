from database import get_connection

def create_account(user_id):
    conn = get_connection()
    cur = conn.cursor()
    
    account_name = input("Enter account name (e.g. Savings account, current account): ")
    try:
        cur.execute("INSERT INTO accounts(user_id, account_name) VALUES(%s,%s)",(user_id, account_name))
        conn.commit()
        print("Account created successfully")
    except Exception as e:
        print("Error:",e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()
        
def view_accounts(user_id):  #user can have multiple accounts like saving and current
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT account_id, account_name, balance FROM accounts WHERE user_id=%s",(user_id,)) #single element tuple
    accounts = cur.fetchall()
    cur.close()
    conn.close()
    
    print("Your Accounts: ")
    for i in accounts: #tuple of 3 (account_id, account_name, balance )
        print(f"ID: {i[0]}, NAME: {i[1]}, BALANCE: {i[2]}")     