#getpass safely reads passwords(hides what you type)
import getpass

#the get_connection function will connect to database
from database import get_connection

def register():
    """Register New User"""
    
    conn = get_connection()  #connect to database (database connection obj)
    cur = conn.cursor()      # create a cursor (used to run postgresql commands)(cursor obj)

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")  #hides input
    
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s,%s)", (username, password))
        # %s are placeholders (NOT Python %s string formatting).
        # psycopg2 will safely replace %s with your values → preventing SQL injection attacks
        #In psycopg2 (Python), you don’t use a semicolon at the end of SQL queries
        #PostgreSQL does not require a semicolon here because execute() is only sending one statement at a time.

        conn.commit()       #commits (saves changes to the database)
        print("Registeration successfull")    
    except Exception as e:  # If something goes wrong (like username already exists)
        print("Error:",e)
        conn.rollback()     #undoes all changes made since the last commit
    finally:                #finally always run even if there is exception
        cur.close()         #after this we cannot execute querries
        conn.close()        #database connection is closed
        
    
def login():
    """User login"""
    
    conn = get_connection()
    cur = conn.cursor()
    
    username = input("username: ")
    password = getpass.getpass("password: ")
    
    cur.execute("SELECT user_id FROM users WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()  #one tuple row i.e user_id will be fetched
    
    cur.close()
    conn.close()
    
    if user:  # an empty tuple is evaluated as false
        print("Login successful")
        return user[0]  #returns user_id
    else:
        print("Invalid credentials")
        return None
        
        
        