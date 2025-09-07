from database import get_connection

def set_budget(user_id):
    conn = get_connection()
    cur = conn.cursor()
    
    category = input("Enter category for budget: ").lower()
    limit_amount = float(input("Enter budget limit: "))
    
    try:
        cur.execute(
            "INSERT INTO budgets(user_id, category, limit_amount) VALUES(%s,%s,%s) ON CONFLICT (user_id, category) DO UPDATE SET limit_amount = %s",(user_id, category, limit_amount,limit_amount)
        )
        #ON CONFLICT - if (user_id and category) i.e. ("9, pasta") is inserted again then ON CONFLICT occures and UPDATEs the limit_amount
        #if no conflict happens, then PostgreSQL just does a normal insert — it doesn’t even touch the ON CONFLICT part.
        conn.commit()
        print("Budget set successfully")
    except Exception as e:
        print("Error: ",e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()
           