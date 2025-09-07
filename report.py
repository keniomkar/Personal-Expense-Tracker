from database import get_connection

def generate_report(user_id):
    conn = get_connection()
    cur = conn.cursor()
    
    # Total expenses per category
    cur.execute(
        "SELECT t.category, SUM(t.amount) FROM transactions t "
        "JOIN accounts a ON t.account_id = a.account_id "
        "WHERE a.user_id = %s GROUP BY t.category",(user_id,) # used , after (user_id,) bcz its a single tuple 
        #give space at last (t ") if dont do then error bcz the strings in () gets concatenated
        #if no space given it will look like this to compiler(transactions tJOIN accounts a)
        
        #SQL’s GROUP BY combines all rows with the same category into one row and sums up their amounts.
    )
    results = cur.fetchall()
    print("\n Report - Total per Category:")
    for i in results:
        print(f" {i[0]}: {i[1]} Rs")
        
    #Total balance across all accounts
    cur.execute(
        "SELECT SUM(balance) From accounts WHERE user_id = %s",(user_id,)
    )
    total_balance = cur.fetchone() #tuple
    print(f"\n Total Balance Across Accounts: {total_balance[0]}")
    
    cur.close()
    conn.close()
    